# -*- coding: utf-8 -*-
from download import YahooJp

nikkei225 = [
  ["1332", u"日本水産", u"水産"],
  ["1333", u"マルハニチロ", u"水産"],
  ["1605", u"国際石油開発帝石", u"鉱業"],
  ["1721", u"コムシスホールディングス", u"建設"],
  ["1801", u"大成建設", u"建設"],
  ["1802", u"大林組", u"建設"],
  ["1803", u"清水建設", u"建設"],
  ["1808", u"長谷工コーポレーション", u"建設"],
  ["1812", u"鹿島建設", u"建設"],
  ["1925", u"大和ハウス工業", u"建設"],
  ["1928", u"積水ハウス", u"建設"],
  ["1963", u"日揮", u"建設"],
  ["2002", u"日清製粉グループ本社", u"食品"],
  ["2269", u"明治ホールディングス", u"食品"],
  ["2282", u"日本ハム", u"食品"],
  ["2432", u"ディー・エヌ・エー", u"サービス"],
  ["2501", u"サッポロホールディングス", u"食品"],
  ["2502", u"アサヒグループホールディングス", u"食品"],
  ["2503", u"キリンホールディングス", u"食品"],
  ["2531", u"宝ホールディングス", u"食品"],
  ["2768", u"双日", u"商社"],
  ["2801", u"キッコーマン", u"食品"],
  ["2802", u"味の素", u"食品"],
  ["2871", u"ニチレイ", u"食品"],
  ["2914", u"日本たばこ産業", u"食品"],
  ["3086", u"J.フロントリテイリング", u"小売業"],
  ["3099", u"三越伊勢丹ホールディングス", u"小売業"],
  ["3101", u"東洋紡", u"繊維"],
  ["3103", u"ユニチカ", u"繊維"],
  ["3105", u"日清紡ホールディングス", u"繊維"],
  ["3289", u"東急不動産ホールディングス", u"不動産"],
  ["3382", u"セブン＆アイ・ホールディングス", u"小売業"],
  ["3401", u"帝人", u"繊維"],
  ["3402", u"東レ", u"繊維"],
  ["3405", u"クラレ", u"化学"],
  ["3407", u"旭化成", u"化学"],
  ["3436", u"SUMCO", u"非鉄・金属"],
  ["3861", u"王子ホールディングス", u"パルプ・紙"],
  ["3863", u"日本製紙", u"パルプ・紙"],
  ["3865", u"北越紀州製紙", u"パルプ・紙"],
  ["4004", u"昭和電工", u"化学"],
  ["4005", u"住友化学", u"化学"],
  ["4021", u"日産化学工業", u"化学"],
  ["4041", u"日本曹達", u"化学"],
  ["4042", u"東ソー", u"化学"],
  ["4043", u"トクヤマ", u"化学"],
  ["4061", u"デンカ", u"化学"],
  ["4063", u"信越化学工業", u"化学"],
  ["4151", u"協和発酵キリン", u"医薬品"],
  ["4183", u"三井化学", u"化学"],
  ["4188", u"三菱ケミカルホールディングス", u"化学"],
  ["4208", u"宇部興産", u"化学"],
  ["4272", u"日本化薬", u"化学"],
  ["4324", u"電通", u"サービス"],
  ["4452", u"花王", u"化学"],
  ["4502", u"武田薬品工業", u"医薬品"],
  ["4503", u"アステラス製薬", u"医薬品"],
  ["4506", u"大日本住友製薬", u"医薬品"],
  ["4507", u"塩野義製薬", u"医薬品"],
  ["4519", u"中外製薬", u"医薬品"],
  ["4523", u"エーザイ", u"医薬品"],
  ["4543", u"テルモ", u"精密機器"],
  ["4568", u"第一三共", u"医薬品"],
  ["4689", u"ヤフー", u"サービス"],
  ["4704", u"トレンドマイクロ", u"サービス"],
  ["4901", u"富士フイルムホールディングス", u"化学"],
  ["4902", u"コニカミノルタ", u"精密機器"],
  ["4911", u"資生堂", u"化学"],
  ["5002", u"昭和シェル石油", u"石油"],
  ["5020", u"JXホールディングス", u"石油"],
  ["5101", u"横浜ゴム", u"ゴム"],
  ["5108", u"ブリヂストン", u"ゴム"],
  ["5201", u"旭硝子", u"窯業"],
  ["5202", u"日本板硝子", u"窯業"],
  ["5214", u"日本電気硝子", u"窯業"],
  ["5232", u"住友大阪セメント", u"窯業"],
  ["5233", u"太平洋セメント", u"窯業"],
  ["5301", u"東海カーボン", u"窯業"],
  ["5332", u"TOTO", u"窯業"],
  ["5333", u"日本碍子", u"窯業"],
  ["5401", u"新日鐵住金", u"鉄鋼"],
  ["5406", u"神戸製鋼所", u"鉄鋼"],
  ["5411", u"ジェイエフイーホールディングス", u"鉄鋼"],
  ["5413", u"日新製鋼", u"鉄鋼"],
  ["5541", u"大平洋金属", u"鉄鋼"],
  ["5631", u"日本製鋼所", u"機械"],
  ["5703", u"日本軽金属ホールディングス", u"非鉄・金属"],
  ["5706", u"三井金属鉱業", u"非鉄・金属"],
  ["5707", u"東邦亜鉛", u"非鉄・金属"],
  ["5711", u"三菱マテリアル", u"非鉄・金属"],
  ["5713", u"住友金属鉱山", u"非鉄・金属"],
  ["5714", u"DOWAホールディングス", u"非鉄・金属"],
  ["5715", u"古河機械金属", u"非鉄・金属"],
  ["5801", u"古河電気工業", u"非鉄・金属"],
  ["5802", u"住友電気工業", u"非鉄・金属"],
  ["5803", u"フジクラ", u"非鉄・金属"],
  ["5901", u"東洋製罐グループホールディングス", u"非鉄・金属"],
  ["6103", u"オークマ", u"機械"],
  ["6113", u"アマダホールディングス", u"機械"],
  ["6301", u"小松製作所", u"機械"],
  ["6302", u"住友重機械工業", u"機械"],
  ["6305", u"日立建機", u"機械"],
  ["6326", u"クボタ", u"機械"],
  ["6361", u"荏原製作所", u"機械"],
  ["6366", u"千代田化工建設", u"機械"],
  ["6367", u"ダイキン工業", u"機械"],
  ["6471", u"日本精工", u"機械"],
  ["6472", u"NTN", u"機械"],
  ["6473", u"ジェイテクト", u"機械"],
  ["6479", u"ミネベア", u"電気機器"],
  ["6501", u"日立製作所", u"電気機器"],
  ["6502", u"東芝", u"電気機器"],
  ["6503", u"三菱電機", u"電気機器"],
  ["6504", u"富士電機", u"電気機器"],
  ["6506", u"安川電機", u"電気機器"],
  ["6508", u"明電舎", u"電気機器"],
  ["6674", u"ジーエス・ユアサコーポレーション", u"電気機器"],
  ["6701", u"日本電気", u"電気機器"],
  ["6702", u"富士通", u"電気機器"],
  ["6703", u"沖電気工業", u"電気機器"],
  ["6752", u"パナソニック", u"電気機器"],
  ["6753", u"シャープ", u"電気機器"],
  ["6758", u"ソニー", u"電気機器"],
  ["6762", u"TDK", u"電気機器"],
  ["6767", u"ミツミ電機", u"電気機器"],
  ["6770", u"アルプス電気", u"電気機器"],
  ["6773", u"パイオニア", u"電気機器"],
  ["6841", u"横河電機", u"電気機器"],
  ["6857", u"アドバンテスト", u"電気機器"],
  ["6902", u"デンソー", u"電気機器"],
  ["6952", u"カシオ計算機", u"電気機器"],
  ["6954", u"ファナック", u"電気機器"],
  ["6971", u"京セラ", u"電気機器"],
  ["6976", u"太陽誘電", u"電気機器"],
  ["6988", u"日東電工", u"化学"],
  ["7003", u"三井造船", u"造船"],
  ["7004", u"日立造船", u"機械"],
  ["7011", u"三菱重工業", u"機械"],
  ["7012", u"川崎重工業", u"造船"],
  ["7013", u"IHI", u"機械"],
  ["7186", u"コンコルディア・フィナンシャルグループ", u"銀行"],
  ["7201", u"日産自動車", u"自動車"],
  ["7202", u"いすゞ自動車", u"自動車"],
  ["7203", u"トヨタ自動車", u"自動車"],
  ["7205", u"日野自動車", u"自動車"],
  ["7211", u"三菱自動車工業", u"自動車"],
  ["7261", u"マツダ", u"自動車"],
  ["7267", u"本田技研工業", u"自動車"],
  ["7269", u"スズキ", u"自動車"],
  ["7270", u"富士重工業", u"自動車"],
  ["7731", u"ニコン", u"精密機器"],
  ["7733", u"オリンパス", u"精密機器"],
  ["7735", u"SCREENホールディングス", u"電気機器"],
  ["7751", u"キヤノン", u"電気機器"],
  ["7752", u"リコー", u"電気機器"],
  ["7762", u"シチズンホールディングス", u"精密機器"],
  ["7911", u"凸版印刷", u"その他製造"],
  ["7912", u"大日本印刷", u"その他製造"],
  ["7951", u"ヤマハ", u"その他製造"],
  ["8001", u"伊藤忠商事", u"商社"],
  ["8002", u"丸紅", u"商社"],
  ["8015", u"豊田通商", u"商社"],
  ["8031", u"三井物産", u"商社"],
  ["8035", u"東京エレクトロン", u"電気機器"],
  ["8053", u"住友商事", u"商社"],
  ["8058", u"三菱商事", u"商社"],
  ["8233", u"高島屋", u"小売業"],
  ["8252", u"丸井グループ", u"小売業"],
  ["8253", u"クレディセゾン", u"その他金融"],
  ["8267", u"イオン", u"小売業"],
  ["8270", u"ユニーグループ・ホールディングス", u"小売業"],
  ["8303", u"新生銀行", u"銀行"],
  ["8304", u"あおぞら銀行", u"銀行"],
  ["8306", u"三菱UFJフィナンシャル・グループ", u"銀行"],
  ["8308", u"りそなホールディングス", u"銀行"],
  ["8309", u"三井住友トラスト・ホールディングス", u"銀行"],
  ["8316", u"三井住友フィナンシャルグループ", u"銀行"],
  ["8331", u"千葉銀行", u"銀行"],
  ["8354", u"ふくおかフィナンシャルグループ", u"銀行"],
  ["8355", u"静岡銀行", u"銀行"],
  ["8411", u"みずほフィナンシャルグループ", u"銀行"],
  ["8601", u"大和証券グループ本社", u"証券"],
  ["8604", u"野村ホールディングス", u"証券"],
  ["8628", u"松井証券", u"証券"],
  ["8630", u"損保ジャパン日本興亜ホールディングス", u"保険"],
  ["8725", u"MS＆ADインシュアランスグループホールディングス", u"保険"],
  ["8729", u"ソニーフィナンシャルホールディングス", u"保険"],
  ["8750", u"第一生命保険", u"保険"],
  ["8766", u"東京海上ホールディングス", u"保険"],
  ["8795", u"T＆Dホールディングス", u"保険"],
  ["8801", u"三井不動産", u"不動産"],
  ["8802", u"三菱地所", u"不動産"],
  ["8804", u"東京建物", u"不動産"],
  ["8830", u"住友不動産", u"不動産"],
  ["9001", u"東武鉄道", u"鉄道・バス"],
  ["9005", u"東京急行電鉄", u"鉄道・バス"],
  ["9007", u"小田急電鉄", u"鉄道・バス"],
  ["9008", u"京王電鉄", u"鉄道・バス"],
  ["9009", u"京成電鉄", u"鉄道・バス"],
  ["9020", u"東日本旅客鉄道", u"鉄道・バス"],
  ["9021", u"西日本旅客鉄道", u"鉄道・バス"],
  ["9022", u"東海旅客鉄道", u"鉄道・バス"],
  ["9062", u"日本通運", u"陸運"],
  ["9064", u"ヤマトホールディングス", u"陸運"],
  ["9101", u"日本郵船", u"海運"],
  ["9104", u"商船三井", u"海運"],
  ["9107", u"川崎汽船", u"海運"],
  ["9202", u"ANAホールディングス", u"空運"],
  ["9301", u"三菱倉庫", u"倉庫"],
  ["9412", u"スカパーJSATホールディングス", u"通信"],
  ["9432", u"日本電信電話", u"通信"],
  ["9433", u"KDDI", u"通信"],
  ["9437", u"NTTドコモ", u"通信"],
  ["9501", u"東京電力ホールディングス", u"電気"],
  ["9502", u"中部電力", u"電気"],
  ["9503", u"関西電力", u"電気"],
  ["9531", u"東京瓦斯", u"ガス"],
  ["9532", u"大阪瓦斯", u"ガス"],
  ["9602", u"東宝", u"サービス"],
  ["9613", u"エヌ・ティ・ティ・データ", u"通信"],
  ["9681", u"東京ドーム", u"サービス"],
  ["9735", u"セコム", u"サービス"],
  ["9766", u"コナミホールディングス", u"サービス"],
  ["9983", u"ファーストリテイリング", u"小売業"],
  ["9984", u"ソフトバンクグループ", u"通信"],
]


def brand_name(code):
    for (target_brand_code, target_brand_name, _) in nikkei225:
        if code == target_brand_code:
            return target_brand_name
    return ''


if __name__ == '__main__':
    for (i, brand) in enumerate(nikkei225):
        print '{} / {}'.format(i + 1, len(nikkei225)), brand[0], brand[1]
        YahooJp(brand[0])
