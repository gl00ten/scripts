rootDir=$(pwd)
for d in $(cat dir_list.txt)
do
  cp reverse_videos_in_curr_dir.bash $d/
  cd $d
  bash reverse_videos_in_curr_dir.bash
  rm $d/reverse_videos_in_curr_dir.bash
  cd $rootDir
done
