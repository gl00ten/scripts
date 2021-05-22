set -x

mkdir -p split/reverse
mkdir -p reversed/before_join
for i in $(ls *MTS)
do
  ffmpeg -i $i -c copy -map 0 -segment_time 00:00:30 -f segment split/output%03d.mp4
  for f in $(ls split/ | grep out);do ffmpeg -i $(pwd)/split/$f -crf 20 -vf reverse split/reverse/$f;done
  for f in $(ls split/reverse | sort -r);do echo file \'$(pwd)/split/reverse/$f\' >> to_concatenate.txt;done
  ffmpeg -f concat -safe 0 -i to_concatenate.txt -c copy reversed/before_join/$i.mp4
  rm -r split
  rm to_concatenate.txt
  mkdir -p split/reverse
done
for f in $(ls reversed/before_join | sort -r);do echo file \'$(pwd)/reversed/before_join/$f\' >> to_concatenate.txt;done
ffmpeg -f concat -safe 0 -i to_concatenate.txt -c copy reversed/joined.mp4
rm -r split
rm to_concatenate.txt
rm -r reversed/before_join
