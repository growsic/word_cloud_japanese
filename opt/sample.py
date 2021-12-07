
#使用するモジュールをimport
import wordcloud, codecs
 
#テキストファイルを読み込み
file = codecs.open('opt/speech.txt', 'r', 'utf-8', 'ignore')
text = file.read()
 
#テキストからwordcloudを生成
wordc = wordcloud.WordCloud(background_color='white', width=800, height=600).generate(text)
 
#画像ファイルとして保存
wordc.to_file('opt/wordcloud.png')