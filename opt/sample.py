
#使用するモジュールをimport
import wordcloud, codecs, MeCab
 
#テキストファイルを読み込み
file = codecs.open('opt/speech.txt', 'r', 'utf-8', 'ignore')
text = file.read()
 
m = MeCab.Tagger('')
parsed = m.parse(text)
splitted = ' '.join([x.split('\t')[0] for x in parsed.splitlines()[:-1]])

fpath = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"
#テキストからwordcloudを生成
wordc = wordcloud.WordCloud(
    font_path=fpath,
    background_color='white',
     width=800, 
     height=600).generate(splitted)
 
#画像ファイルとして保存
wordc.to_file('opt/wordcloud.png')

