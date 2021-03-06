cd /xy/src/MutualFundAnalysis/
ver=`date +%Y%m%d%H`
docker build -t mutualfundanalysis:$ver .
containerId=`docker ps | grep mutualfundanalysis: | awk '{print $1}'`
imageId=`docker ps | grep mutualfundanalysis: | awk '{print $2}'`
if [ -n "$containerId" ]; then
  docker stop $containerId
  docker rm $containerId
fi
if [ -n "$imageId" ]; then
  docker rmi $imageId
fi

docker run  -d -p 8000:8000 \
    --name=mutualfundanalysis-$ver mutualfundanalysis:$ver
