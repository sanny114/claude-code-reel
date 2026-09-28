# Claude Code 紹介リール（15秒）

Claude Codeを知らない人に向けた15秒のモーショングラフィックス。映像も音も、すべてコードで1フレームずつ書いたもの。

- 公開ページ: https://sanny114.github.io/claude-code-reel/
- `claude_code_reel.mp4` — 本編（1920×1080 / 60fps / 音声つき）
- `live.html` — Canvas版。ブラウザでリアルタイムに描画（`audio.wav` を置くと音つき）
- `src/reel.html` — 映像のソース（`live.html` と同じ）。`?render` を付けると書き出し用に `window.renderAt(t)` だけを公開する
- `src/sfx_reel.py` — サウンドトラック `audio.wav` をnumpyで合成

書き出し: 120fpsの連番PNGをPlaywrightで書き出し、`ffmpeg -framerate 120 -i frames/f%05d.png -i audio.wav -vf "tmix=frames=2,fps=60,format=yuv420p" -c:v libx264 -crf 22 -c:a aac claude_code_reel.mp4`

フォント（`fonts/`）: Noto Sans JP / Anton / JetBrains Mono（SIL Open Font License）。マスコットはオリジナルのドット絵。制作: Claude Code。
