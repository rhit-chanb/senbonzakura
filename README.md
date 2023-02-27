# senbonzakura
##### Split YouTube videos or audio based on timestamps exported from ytstampplayer

The file `data.json` contains the tag data that will be used to split the video/audio into parts. 
Example formatting can be found in `data_example.json` if you want to make your own.

To run the script, cd into the root directory and run this in a terminal window:

```python main.py {video_url}```

Use ```python main.py {video_url} -v``` if you would like to split as video instead of audio.

Output is written to the `output` folder.
