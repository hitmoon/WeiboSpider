#!/bin/bash
#set -x

echo "generating query string ..."
Q='db.Tweets.aggregate([{$replaceRoot: {newRoot: {user: "$nick_name", time: "$created_at", content: "$content", url: "$weibo_url", repost_num: "$repost_num", like_num: "$like_num"}}}, {$project: {time: {$dateFromString: {dateString:"$time", timezone: "Asia/Shanghai"}}, user: 1, content: 1, url: 1, repost_num: 1, like_num: 1}}, {$match: {time: {$gte: ISODate()}}}, {$sort: {like_num: -1}}, {$out: "news"}])'

DATE=$(date -d "yesterday 00:00" +"%Y-%m-%dT%H:%M:%S.0Z")

echo "$Q" | sed 's@ISODate()@ISODate("'$DATE'")@' > q.js


echo "generate temp database"
~/Mongo/bin/mongo Sina q.js

echo "export data"
~/Mongo/bin/mongoexport -d Sina -c news \
-f user,time,content,url,like_num --type=csv > out.csv

echo "drop temp database"
echo "db.news.drop()" > drop.js
~/Mongo/bin/mongo Sina drop.js

rm -f q.js drop.js
