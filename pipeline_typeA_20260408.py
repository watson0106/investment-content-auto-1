"""
investment-content-auto-1 タイプA記事（2026-04-08）
停戦協定で日経平均が爆上げの中、任天堂はなぜ下落しているのか？
"""
import json
import os
import subprocess
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
DATE_STR       = "2026-04-08"
THUMBNAIL_PATH = Path(__file__).parent / f"output/images/thumbnail_{DATE_STR}.png"
ARTICLE_PATH   = Path(__file__).parent / f"output/article_{DATE_STR}.md"

TITLE = "停戦協定で日経平均が爆上げの中、任天堂はなぜ下落しているのか？"

BODY = """## 結論：米・イランの停戦は「円高要因」であり、任天堂は海外売上が7割を超える「円高に最も弱い銘柄」の一つである

2026年4月8日朝、パキスタンが仲介した**米国・イランの2週間停戦合意**が発表されました。この一報を受けて日経平均株価は前日比+2,878円（+5.39%）の56,308円まで急騰し、歴代3位の上げ幅を記録しました。トヨタ・三菱商事・川崎重工といった銘柄が一斉に買われ、相場全体が浮揚しました。その中で、任天堂（7974）は逆行安。同日-137円（-1.55%）と下落し、「市場が上がっているのに、なぜ任天堂だけ下がっているのか」と疑問に思った方も多かったと思います。

答えはシンプルです。**米・イラン停戦は円高要因であり、任天堂は「円高に最も敏感な銘柄」の一つだからです。**

日経平均が上がっているときに個別株が逆行安する現象は珍しくありません。むしろ、「なぜ市場全体と違う動きをするのか」を構造から理解できるかどうかが、個人投資家の実力差になります。この任天堂の逆行安を入口に、「停戦ラリーの恩恵を受ける銘柄」と「恩恵を受けない銘柄」を分ける本質的な違いを解説します。

__IMAGE_0__

### 理由1：米・イラン停戦は「円高トリガー」になる

地政学的リスクが高まると、投資家は「有事の円買い」をします。円は安全資産とみなされているため、中東情勢の緊張・紛争・金融不安のタイミングで円が買われ、円高になります。

今回の停戦の背景は、米・イラン間の核交渉とホルムズ海峡周辺での緊張です。中東は原油輸送の要衝であり、イラン絡みのリスクが高まると「有事の円買い」と「原油価格上昇」が同時に起きます。パキスタン仲介による2週間停戦が合意されたことで、このリスクプレミアムが一気に剥落しました。

**停戦直後は円の「有事プレミアム」が剥落して適正水準に戻ろうとする動きが起きます。** 日本は原油を100%近く輸入しており、原油価格の下落→輸入コスト低下→貿易収支改善→円高という波及経路があります。日経平均は「景気回復期待」で上昇しましたが、為替は円高方向に振れました。

今回の局面では、地政学リスクが高かった時期に積み上がった円のショートポジション（円売り）が一斉に解消され、一部の輸出企業には「円高懸念」がのしかかりました。任天堂はその最右翼です。

### 理由2：任天堂の株価は「足元の実績」よりも「Switch 2の期待値」で動いている

任天堂の売上高の約75%は海外から来ています（2025年3月期実績）。北米・欧州での「ゼルダ」「マリオ」「ポケモン」関連ソフト・ハードの販売が主軸です。

円安になれば、ドル建て・ユーロ建ての売上が円換算で増えます。理論的には任天堂にも円安の恩恵はあります。**しかし株式市場は「将来の期待値」で動きます。** 今回の逆行安の本質は為替の問題だけではなく、「停戦による市場センチメントの変化」が任天堂株の需給を崩したことにあります。

停戦ラリーでは機関投資家が「リスクオン」に転換し、ポートフォリオをシクリカル株（景気敏感株）に積極的にシフトします。素材・エネルギー・防衛・自動車・金融といった「景気が回復すれば直接恩恵を受けるセクター」に資金が集中するのです。

**任天堂はゲーム会社であり、景気の良し悪しとは比較的無関係に売上が立つ「ディフェンシブ消費株」に分類されます。** 停戦で景気回復期待が高まると、ディフェンシブ株は「もう安全資産を持っておく必要はない」と判断されて売られます。これがセクターローテーションによる逆行安の正体です。

__IMAGE_1__

### 理由3：Switch 2の関税リスクとハードウェアサイクルの不透明感

任天堂株の動きを語る上で、もう一つ見逃せない材料があります。**Nintendo Switch 2（2026年6月5日発売予定、米国価格$449.99）はベトナムで製造されています。** 米国がベトナム産製品に高関税を課した場合、Switch 2の価格競争力や採算に直撃します。

米・イラン停戦が合意されると、トランプ政権の外交・通商政策の次の焦点が「アジア」に移る可能性があります。市場の一部では「中東問題が片付いた分、対中・対アジア関税政策が再加速するのではないか」という懸念が浮上しました。任天堂の製造拠点であるベトナムは、対米関税の「次の標的」として警戒されているのです。

また、過去のデータを見ると、任天堂株は新ハードの**発売直前に上昇し、発売後に「材料出尽くし」で下落する傾向**があります。

- Wii（2006年12月発売）：発売前に急騰 → 発売後に「期待の巻き戻し」で下落
- Nintendo Switch（2017年3月発売）：発売前の期待買いで株価上昇 → 発売直後に一時調整

2026年4月はSwitch 2発売の約2ヶ月前です。停戦ラリーという外部イベントが重なったことで、「シクリカル株に乗り換えたい機関投資家が任天堂を売るタイミングを得た」という構図になっています。

### 任天堂の「海外売上比率」が高いことは、長期では強みだが短期では弱みになる

任天堂の海外売上比率は約75%です。長期的には大きな強みです。「マリオ」「ゼルダ」「ポケモン」というIPは世界中で認知されており、円安局面では自動的に円建て利益が増えます。

しかし短期的には、この高い海外比率が「為替に翻弄される株」になるリスクを生みます。

円が1円動くと任天堂の営業利益は約40億円変わるとされています（会社発表のレート感応度）。停戦後の為替の動きが任天堂の業績予想をリアルタイムで書き換えていきます。市場参加者はこのレート感応度を頭に入れながら、「今の為替水準なら任天堂の通期利益は何億円になるか」を即座に再計算しています。

**「任天堂が上がっていない」のは、停戦後の為替の方向感が定まらない中で、機関投資家が様子見をしているからでもあります。** 停戦直後の混乱期は、為替がどちらに動くかの見極めに時間がかかります。その分だけ、任天堂株は方向感を失いやすいのです。

__IMAGE_2__

## 投資家として、どこに注目するか

### 「停戦ラリー」の恩恵を受ける銘柄と受けない銘柄を分ける3つの軸

米・イランの停戦合意のような地政学リスク後退のニュースが出たとき、以下の3軸で銘柄を仕分けすると判断しやすくなります。

**軸1：景気感応度（シクリカルかディフェンシブか）**
停戦 → 景気回復期待 → シクリカル株（鉄鋼・化学・自動車・金融）に資金流入。ディフェンシブ株（食品・医薬品・ゲーム・通信）は相対的に売られやすくなります。

**軸2：為替感応度（円安恩恵か円高恩恵か）**
今回の停戦後の為替は円高方向。輸出企業は打撃を受けます。任天堂は輸出企業ですが「期待株」の性格が強く、足元の為替より将来の成長期待が株価を動かす比重が高いです。

**軸3：個別テーマの強さ（ハードサイクル・関税リスク・新製品）**
マクロ要因がどちらに動いても、個別テーマが強い銘柄は独自の動きをします。任天堂の場合はSwitch 2（6月5日発売）のサイクルと、ベトナム製造による関税リスクが最大のテーマです。

### 任天堂株の長期視点

任天堂を長期保有している投資家にとって、今回の逆行安は「構造的な問題」ではありません。停戦ラリーによるセクターローテーションと、ハードサイクルの端境期・関税懸念が重なった「短期的な需給の悪化」です。

任天堂のIPポートフォリオ（マリオ・ゼルダ・ポケモン・スプラトゥーン・どうぶつの森）の価値は、短期の株価には反映されない長期的な競争優位です。Switch 2が市場に受け入れられ、関税問題が解決されれば、次の上昇サイクルが始まります。

一方、「停戦ラリーに乗って短期利益を取りたい」という投資家には、任天堂よりも素材・エネルギー・防衛・重工業セクターの方が適しています。投資スタイルと保有期間に応じて「今、任天堂を持ち続けるべきか」を判断することが大切です。

## まとめ

・2026年4月8日、パキスタン仲介による米・イラン2週間停戦合意で日経平均は+2,878円（+5.39%）の56,308円まで急騰（歴代3位）
・任天堂（7974）は同日-137円（-1.55%）と逆行安
・停戦 → 有事プレミアム剥落 → 円高圧力 → 海外売上75%超の任天堂に業績下押し懸念
・停戦ラリーで機関投資家がシクリカル株にシフト → ディフェンシブ株の任天堂は売られやすくなった
・Switch 2（6月5日発売、米国$449.99）はベトナム製造 → 対アジア関税リスクも懸念材料
・「日経平均が上がっているのに個別株が下がる」現象は、セクターローテーションの典型例として覚えておく価値があります""".strip()


IMAGE_MODELS = [
    "gemini-3-pro-image-preview",
    "gemini-3.1-flash-image-preview",
    "gemini-2.5-flash-image",
]


def generate_image(prompt, path):
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=GEMINI_API_KEY)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    for model in IMAGE_MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(response_modalities=["image", "text"]),
            )
            for part in response.candidates[0].content.parts:
                if part.inline_data:
                    with open(path, "wb") as f:
                        f.write(part.inline_data.data)
                    print(f"    [{model}] 生成完了: {Path(path).name}")
                    return path
        except Exception as e:
            print(f"    [WARN] {model} 失敗: {e}")

    try:
        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=prompt,
            config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio="16:9"),
        )
        if response.generated_images:
            with open(path, "wb") as f:
                f.write(response.generated_images[0].image.image_bytes)
            print(f"    [imagen-4.0 fallback] 生成完了: {Path(path).name}")
            return path
    except Exception as e:
        print(f"    [WARN] imagen-4.0 失敗: {e}")
    return None


# ─── IMAGE_0: 停戦→円高→任天堂株への影響フロー ──────────────
def generate_ceasefire_flow():
    print("[IMAGE_0] 米・イラン停戦→円高→任天堂株影響フロー図生成中...")
    prompt = """投資ブログ記事用のフロー図を作成してください。

【テーマ】米・イラン停戦合意が任天堂株に与える影響のメカニズム

【内容：左から右に流れる4ステップ図】
ステップ1「米・イラン2週間停戦合意（パキスタン仲介）」：
・中東地政学リスクが後退
・原油価格下落・リスクオン相場に転換

ステップ2「為替の動き」：
・有事の円買いポジションが巻き戻し
・原油安→日本の貿易収支改善→円高圧力
・円高方向に振れる

ステップ3「セクターローテーション」：
・シクリカル株（自動車・鉄鋼・金融）に資金流入
・ディフェンシブ株・成長期待株は相対的に売られる

ステップ4「任天堂株への影響」：
・海外売上75%超→円高で業績下押し
・Switch 2ベトナム製造→関税リスク浮上
・結果：日経平均+2878円（+5.39%） だが任天堂-137円（-1.55%）逆行安

【デザイン要件】
・ダークネイビー背景にホワイト・ゴールドのテキスト
・タイトル「米・イラン停戦が任天堂株を下げるメカニズム」を上部に日本語で
・すべてのテキストは日本語
・プロフェッショナルな金融メディア品質、16:9横長
"""
    return generate_image(prompt, str(Path(__file__).parent / f"output/images/nintendo_flow_{DATE_STR}.png"))


# ─── IMAGE_1: セクターローテーション図 ───────────────────────
def generate_sector_rotation():
    print("[IMAGE_1] セクターローテーション図生成中...")
    prompt = """投資ブログ記事用の比較インフォグラフィックを作成してください。

【テーマ】停戦ラリーで「買われるセクター」と「売られるセクター」

【左側：停戦で買われるセクター（緑・上昇矢印）】
・自動車（景気回復→輸出拡大期待）
・鉄鋼・非鉄金属（資源需要回復期待）
・防衛・重工業（復興需要）
・銀行・金融（景気回復→貸出増加期待）
・エネルギー（原油安で採算改善の日本企業）

【右側：停戦で売られるセクター（赤・下降矢印）】
・ゲーム・エンタメ（ディフェンシブ株として保有されていたが不要に）
・食品・日用品（同上）
・医薬品（同上）
・ベトナム製造の製品（関税リスク再浮上）

中央に「米・イラン停戦合意」のアイコンを置き、左右に影響矢印を表示。
任天堂（ゲーム・ベトナム製造）が右側（売られる）に分類されることをハイライト。

【デザイン要件】
・左右の対比レイアウト
・タイトル「停戦ラリー：買われるセクター vs 売られるセクター」を上部に日本語で
・すべてのテキストは日本語
・白背景、プロフェッショナルな金融メディア品質、16:9横長
"""
    return generate_image(prompt, str(Path(__file__).parent / f"output/images/nintendo_sector_{DATE_STR}.png"))


# ─── IMAGE_2: 任天堂の売上地域別構成比 ──────────────────────
def generate_nintendo_revenue():
    print("[IMAGE_2] 任天堂売上構成比グラフ生成中...")
    prompt = """投資ブログ記事用の円グラフ（ドーナツチャート）を作成してください。

【テーマ】任天堂の売上高・地域別構成比（2025年3月期）

【データ】
・米州：約45%（ブルー）
・欧州：約25%（グリーン）
・その他海外：約5%（パープル）
・日本国内：約25%（オレンジ）

海外計（米州＋欧州＋その他）：約75%を目立たせる。
「海外売上75%超」というラベルを大きく強調表示。

【追加要素】
・チャートの右側に「1円の円高で営業利益が約40億円減少」という注釈テキストボックスを置く
・「Switch 2はベトナム製造→米国関税の影響を受ける可能性」という注記を下部に追加
・為替感応度の高さと関税リスクを視覚的に表現する

【デザイン要件】
・白背景、グリッドなし
・タイトル「任天堂の売上地域構成（2025年3月期）」を上部に日本語で
・凡例・ラベルはすべて日本語
・プロフェッショナルな金融メディア品質、16:9横長
"""
    return generate_image(prompt, str(Path(__file__).parent / f"output/images/nintendo_revenue_{DATE_STR}.png"))


# ─── サムネイル ──────────────────────────────────────────────
def generate_thumbnail():
    print("[THUMB] サムネイル生成中...")
    prompt = f"""投資ブログのカバー画像（アイキャッチ）を作成してください。

【記事タイトル】
{TITLE}

【デザイン要件】
1. 背景：ダークネイビーベース、日経平均急騰チャートと任天堂キャラクターシルエットの対比ビジュアル（発光エフェクト）
2. 中央：巨大な発光する「？」マーク（白またはゴールド）
3. 上部：白の極太フォントでタイトルテキスト「停戦協定で日経平均が爆上げの中、任天堂はなぜ下落しているのか？」（半透明オーバーレイ背景付き）
4. テキストはすべて日本語で鮮明に読めること
5. 16:9横長、高解像度
"""
    path = generate_image(prompt, str(THUMBNAIL_PATH))
    if path:
        from PIL import Image
        img = Image.open(path)
        img = img.resize((1920, 1006), Image.LANCZOS)
        img.save(path)
        print(f"    [THUMB] 1920×1006px にリサイズ完了")
    return path


# ─── 記事保存 ────────────────────────────────────────────────
def save_article():
    with open(ARTICLE_PATH, "w") as f:
        f.write(f"# {TITLE}\n\n{BODY}")
    print(f"記事保存: {ARTICLE_PATH}（{len(BODY)}文字）")


# ─── stock-analysis-auto 用 JSON 生成 ────────────────────────
JSON_PATH = Path(__file__).parent / f"output/article_{DATE_STR}.json"

def save_article_json():
    """stock-analysis-auto が読める形式の JSON を output/ に保存する"""
    data = {
        "title": TITLE,
        "article": f"# {TITLE}\n\n{BODY}",
        # image_paths に銘柄コードパターンを含めることで extractor が 7974 を検出する
        "image_paths": ["output/charts/7974_chart.png"],
        "source_news": {
            "news1": {
                "source": "独自取材",
                "title": "米・イラン2週間停戦合意（パキスタン仲介）、日経平均+2878円、任天堂逆行安-137円",
                "summary": "2026年4月8日朝、パキスタンが仲介した米国・イランの2週間停戦合意が発表。日経平均は+2878円（+5.39%）の56308円まで急騰（歴代3位）。任天堂（7974）は円高懸念・セクターローテーション・Switch 2関税リスクで-137円（-1.55%）の逆行安。",
            }
        },
        "skip_stock": False,
    }
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"JSON保存: {JSON_PATH}")
    return str(JSON_PATH.resolve())


# ─── stock-analysis-auto 実行 ────────────────────────────────
def run_stock_analysis(article_json_path: str):
    sa_main = os.path.expanduser("~/stock-analysis-auto/src/main.py")
    if not os.path.exists(sa_main):
        print("  [SKIP] ~/stock-analysis-auto が見つかりません")
        return
    sa_env = {k: v for k, v in os.environ.items()
              if k != "CLAUDECODE" and not k.startswith("CLAUDE_CODE_")}
    sa_env["PATH"] = "/opt/homebrew/bin:/usr/local/bin:" + sa_env.get("PATH", "/usr/bin:/bin")
    print(f"\n株式短期分析パイプライン 実行中（任天堂 7974）...")
    result = subprocess.run(
        [sys.executable, sa_main, "--article", article_json_path],
        env=sa_env,
        cwd=os.path.expanduser("~/stock-analysis-auto/src"),
        timeout=1800,
    )
    if result.returncode != 0:
        print(f"  [WARN] 株式短期分析が非ゼロ終了 (code={result.returncode})")


# ─── note投稿 ────────────────────────────────────────────────
def post_to_note(paths):
    sys.path.insert(0, '/Users/watson/investment-content-auto/src')
    from post_to_note import post_article

    tags = ["投資", "株式投資", "日本株", "任天堂", "米イラン停戦", "セクターローテーション", "為替"]
    image_paths = [str(Path(p).resolve()) for p in paths if p]
    cover = str(THUMBNAIL_PATH.resolve()) if THUMBNAIL_PATH.exists() else None

    print("note に投稿中...")
    url = post_article(
        title=TITLE,
        body=BODY,
        image_paths=image_paths,
        tags=tags,
        cover_path=cover,
        headless=False,
        auto_publish=False,
    )
    print(f"\n投稿完了: {url}")
    return url


if __name__ == "__main__":
    save_article()
    article_json_path = save_article_json()

    # 株式短期分析（有料note）
    try:
        run_stock_analysis(article_json_path)
    except subprocess.TimeoutExpired:
        print("  [WARN] 株式短期分析タイムアウト（30分）")
    except Exception as e:
        print(f"  [WARN] 株式短期分析失敗（無料記事は継続）: {e}")

    # chromedriver プロセスを一旦クリア（stock-analysis-auto と競合防止）
    os.system("pkill -f 'undetected_chromedriver|chromedriver' 2>/dev/null; sleep 3")

    # 画像生成
    flow_path    = generate_ceasefire_flow()   # IMAGE_0
    sector_path  = generate_sector_rotation()  # IMAGE_1
    revenue_path = generate_nintendo_revenue() # IMAGE_2
    thumb_path   = generate_thumbnail()

    # 無料note投稿
    post_to_note([flow_path, sector_path, revenue_path])
