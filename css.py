def get_stylesheet():
    return """
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #e0f2f7, #c1e7f0); /* より明るく穏やかなグラデーション */
    margin: 0;
    padding: 20px; /* 全体にパディングを追加 */
    text-align: center;
    min-height: 100vh; /* 少なくともビューポートの高さにする */
    display: flex; /* flexboxを使ってコンテンツを中央に寄せる */
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.container { /* 新しいコンテナクラス */
    background-color: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15); /* より深みのある影 */
    max-width: 500px; /* 最大幅を設定 */
    width: 90%; /* 小さい画面での対応 */
}

h1 {
    color: #2c3e50;
    margin-top: 0; /* コンテナ内で調整 */
    margin-bottom: 30px;
    font-size: 2.8em; /* 少し大きく */
    text-shadow: 1px 1px 2px rgba(0,0,0,0.05); /* 軽いテキストシャドウ */
}

a {
    display: inline-block;
    padding: 18px 30px; /* パディングを増やす */
    margin: 15px 10px;
    background: #3498db;
    color: white;
    text-decoration: none;
    font-size: 1.3em; /* 少し大きく */
    border-radius: 30px; /* より丸いボタン */
    box-shadow: 0 6px 12px rgba(0,0,0,0.2); /* 影を強化 */
    transition: background 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease; /* 影にもトランジション */
    position: relative; /* 疑似要素のために必要 */
    overflow: hidden; /* 疑似要素がはみ出さないように */
}

a:hover {
    background: #2980b9;
    transform: translateY(-3px) scale(1.03); /* 少し上に移動し、わずかに拡大 */
    box-shadow: 0 10px 20px rgba(0,0,0,0.3); /* ホバー時の影をさらに強調 */
}

a:active {
    transform: translateY(0); /* クリック時は元の位置に戻す */
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

/* ボタンにわずかな光沢を追加 */
a::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255,255,255,0.1);
    z-index: 1;
    transform: translateX(-100%) skewX(-15deg);
    transition: transform 0.3s ease-out;
}

a:hover::before {
    transform: translateX(100%) skewX(-15deg);
}

/* リンク間のスペースを広げるための追加スタイル */
.button-group {
    margin-top: 30px;
}
"""