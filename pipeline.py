"""
investment-content-auto-1 メインパイプライン
1. 記事テキストを受け取る
2. Gemini Imagen で記事テーマの画像を生成
3. note に下書き投稿
"""
import os, sys, re, json, datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
DATE_STR = datetime.date.today().strftime("%Y-%m-%d")
IMAGE_PATH = Path(__file__).parent / f"output/images/image_{DATE_STR}.png"
ARTICLE_PATH = Path(__file__).parent / f"output/article_{DATE_STR}.md"

# ─── 記事本文 ────────────────────────────────────────────────
TITLE = "欧米株が最高値を更新すると、なぜ翌日の日経平均も上がるのか？"

BODY = """
4月6日（月）の東京市場で、日経平均株価は前日比685円高の52,518円と2025年10月以来の最高値を更新した。前夜にドイツのDAX・イギリスのFTSE100・米S&P500がそろって最高値を更新したことが直接の引き金だ。なぜ欧米株の動きが翌日の日経平均にここまで影響するのか、その仕組みを解説する。

## 結論：日本株は「世界の株高」に引っ張られる構造になっている

### 理由1：海外投資家が日本株の売買の約7割を占めているから

日本の株式市場では、売買の約7割が海外の機関投資家（年金基金・ヘッジファンドなど）によって行われている。

欧米の株式市場が上がると、海外投資家の「リスクを取って投資しよう」という意欲が高まる。その資金が日本株にも流れ込む。

逆に欧米株が下落すると、海外投資家がリスクを避けようとして日本株も売られる。**日本株の値動きが「欧米の後追い」になりやすいのはこのためだ。**

### 理由2：前夜の欧米市場が「翌日の日本市場の先行指標」になるから

日本の株式市場（東証）は午前9時に開く。その時点で欧米市場はすでに前日の取引を終えている。

投資家はその結果を見て「今日の日本株は上がりそうか下がりそうか」を判断し、寄り付き（開場直後の値動き）から反映させる。

4月5日の夜から6日の朝にかけて欧米主要指数がそろって最高値を更新したことが、本日の日経平均685円高の直接的な引き金になった。

### 理由3：先物市場が「夜間に日本株の方向性を決める」から

東証が閉まっている夜間も、大阪取引所の日経225先物は24時間取引されている。欧米株が上がった夜、先物価格もつられて上昇する。

翌朝、東証の現物市場が開くときには「先物がすでに上がっている」状態になっているため、現物株も追随して上昇するという仕組みだ。

## では、欧米株が上がれば日本株は常に上がるのか？

### 例外がある：円高が同時進行するとき

欧米株が上がっても、日本株が上がらない（あるいは下がる）ケースがある。「リスクオンによる円高」が同時に起きるときだ。

**円高になると輸出企業の業績見通しが悪化する**。自動車・機械・電機など輸出に頼る大企業が多い日本株にとって、円高は向かい風になる。このとき「欧米株高＝日本株高」という構図が崩れる。

### 今日の上昇で注目すべきセクター

今日のように「欧米株高＋金利上昇」が重なるときは、以下のセクターの動きに注目したい：

- **金融株（銀行・証券）**：金利上昇で利ざやが拡大し、収益増加期待が高まる
- **エネルギー株**：トランプ大統領によるベネズエラ石油インフラ修復の示唆もあり、資源株に買いが集まった
- **成長株（グロース系）**：金利上昇で将来の利益の割引率が上がるため、相対的に割高になりやすく出遅れることが多い

指数全体が上がっているときでも、すべての銘柄が均等に上がるわけではない。「なぜ上がっているのか」を理解すると、恩恵を受けるセクターが自然に見えてくる。

## まとめ

- 日本株の売買の約7割は海外投資家が担っており、欧米市場の影響を強く受ける
- 欧米株高 → 海外投資家のリスク許容度向上 → 日本株買い、というルートが基本
- ただし円高が重なると輸出株には逆風になり、「欧米高＝日本株高」が崩れる
- 今日の上昇は金融・エネルギーセクターが牽引した

欧米株の終値は毎朝のニュースで確認できる。「昨夜の欧米市場がどうだったか」を習慣的にチェックするだけで、今日の日本株の寄り付きの方向性が見えるようになる。

情報を正確に理解することは、投資の第一歩に過ぎない。
株価は常に「情報の一歩先」を織り込んで動いており、
ニュースを読むだけでは勝てないのが相場の現実だ。
毎週の注目銘柄・具体的な売買シナリオ・エントリー根拠まで踏み込んで解説する有料マガジンはこちら。
「知っている」を「稼げる」に変えたい方はぜひ。
https://note.com/kawasewatson0106/m/me3bdb7d529fc
"""

# ─── Step 1: Gemini Imagen で画像生成 ────────────────────────
def generate_image():
    print("画像生成中（Gemini Imagen）...")
    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=GEMINI_API_KEY)

        prompt = (
            "Tokyo stock market trading floor, digital screens showing green rising charts, "
            "bullish financial market concept, dramatic lighting, no people, no text"
        )

        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
            ),
        )

        if response.generated_images:
            img_bytes = response.generated_images[0].image.image_bytes
            with open(IMAGE_PATH, "wb") as f:
                f.write(img_bytes)
            print(f"  画像保存: {IMAGE_PATH}")
            return str(IMAGE_PATH)
        else:
            print("  画像生成失敗（レスポンスなし）")
            return None
    except Exception as e:
        print(f"  画像生成エラー: {e}")
        return None


# ─── Step 2: note に投稿 ──────────────────────────────────────
def post_to_note(image_path):
    sys.path.insert(0, '/Users/watson/investment-content-auto/src')
    from post_to_note import post_article

    tags = ["投資", "株式投資", "資産運用", "米国株", "日本株", "日経平均", "マクロ経済"]

    # タイトル直下に画像マーカーを挿入
    body = BODY.strip()
    if image_path:
        body = '__IMAGE_0__\n\n' + body
    # 絶対パスに変換（カバー画像設定に必要）
    if image_path:
        image_path = str(Path(image_path).resolve())
    image_paths = [image_path] if image_path else []

    print("note に投稿中...")
    url = post_article(
        title=TITLE,
        body=body,
        image_paths=image_paths,
        tags=tags,
        headless=False,
        auto_publish=False,
    )
    print(f"\n投稿完了: {url}")
    return url


# ─── Step 3: 記事をファイルに保存 ────────────────────────────
def save_article():
    with open(ARTICLE_PATH, "w") as f:
        f.write(f"# {TITLE}\n\n{BODY.strip()}")
    print(f"記事保存: {ARTICLE_PATH}")


if __name__ == "__main__":
    save_article()
    image_path = generate_image()
    post_to_note(image_path)
