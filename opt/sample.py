
#使用するモジュールをimport
import wordcloud, codecs, MeCab
import re

# 集計から除外する出現回数上位の順位閾値
HIGH_FREQUENCY_WORD_COUNT_THREHOULD = 30

def is_target_word(word: str, word_type: str) -> bool:
    """
    集計対象の単語か
    ノイズになるパータンの文字列の除去が目的
    """

    # ひらがなのみから構成される単語を除外
    pattern = re.compile(r'[あ-ん]+')
    if pattern.fullmatch(word):
        return False

    # １文字単語は除外
    if len(word) == 1:
        return False
    return True
 
#テキストファイルを読み込み
file = codecs.open('opt/speech.txt', 'r', 'utf-8', 'ignore')
text = file.read()

#テキストからwordcloudを生成
fpath = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"
wordc = wordcloud.WordCloud(
    font_path=fpath,
    background_color='white',
     width=800, 
     height=600)

# 形態素解析した文字列に変換 
m = MeCab.Tagger('')

# 出現頻度が高いワードを除外
tab_separated_str = ' '.join([x.split('\t')[0] for x in m.parse(text).splitlines()[:-1] if is_target_word(x.split('\t')[0], x.split('\t')[1].split(',')[0])])
frequency_dict = wordc.process_text(tab_separated_str)
# 出現上位の単語を頻度とともに出力
print([x for x in sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)[:100]])
high_frequency_word_list = [x[0] for x in sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)[:HIGH_FREQUENCY_WORD_COUNT_THREHOULD]]
# 出現上位のワードを省きwordcloud用のタブ区切り文字列を生成
tab_separated_str = ' '.join([x.split('\t')[0] for x in m.parse(text).splitlines()[:-1] if x.split('\t')[0] not in high_frequency_word_list and is_target_word(x.split('\t')[0], x.split('\t')[1].split(',')[0])])

 
#画像ファイルとして保存
wordc.generate(tab_separated_str).to_file('opt/wordcloud.png')

