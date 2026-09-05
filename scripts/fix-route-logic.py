from pathlib import Path
p = Path('index.html')
s = p.read_text()
# Keep the answer choices independent from the visual route direction.
old = """function choices(){const dirs=['U','R','D','L'],correctDir=state.route[state.step+1].dir;
  const correctIndex=dirs.indexOf(correctDir);
  const used=new Set(),vals=Array(4);
  const correct=getCorrectValue();
  vals[correctIndex]=correct;used.add(correct);
  for(let i=0;i<4;i++){
    if(i===correctIndex)continue;
    const d=getDistractor(used);used.add(d);vals[i]=d;
  }
  state.sceneCorrect=correct;
  return dirs.map((dir,i)=>({dir,value:vals[i],ok:i===correctIndex}));
}"""
new = """function choices(){
  const dirs=['U','R','D','L'];
  const used=new Set(),vals=Array(4);
  const correct=getCorrectValue();
  const correctIndex=rnd(0,3);
  vals[correctIndex]=correct;used.add(correct);
  for(let i=0;i<4;i++){
    if(i===correctIndex)continue;
    const d=getDistractor(used);used.add(d);vals[i]=d;
  }
  state.sceneCorrect=correct;
  return dirs.map((dir,i)=>({dir,value:vals[i],ok:i===correctIndex}));
}"""
if old in s:
    s=s.replace(old,new)
# Move the instructional advice out of the fantasy map so it never overlaps the choices.
s=s.replace('.routeHint{position:absolute;z-index:8;left:50%;top:15px;transform:translateX(-50%);background:#071a12b8;color:#fff;border:1px solid #ffffff44;border-radius:999px;padding:7px 12px;font-size:12px;font-weight:900}', '.gameHint{margin:0 0 8px;padding:9px 13px;border:2px solid var(--line);border-radius:14px;background:#fff;color:var(--dark);font-size:13px;font-weight:900;text-align:center}')
s=s.replace('.routeHint{font-size:10px;top:47px}', '')
s=s.replace('<div class="mazeShell"><div id="scene" class="scene">', '<div class="gameHint">正しい数字を選ぼう。正解すると、ナビキャラとルートが先へ進むよ。</div><div class="mazeShell"><div id="scene" class="scene">')
s=s.replace('<div class="routeHint">正解の道をえらんで ルートを進もう！</div>', '')
# Keep the wording aligned with the 4-choice learning design.
s=s.replace('4つの数字から、条件に合う道を見つけよう。正解するたびに、ナビキャラと冒険ルートが先へ進むよ。','4つの数字から、条件に合う数字を見つけよう。正解するたびに、ナビキャラと冒険ルートが先へ進むよ。')
s=s.replace('<div class="card"><b>4方向</b><small>上・右・下・左</small></div>','<div class="card"><b>4択</b><small>正しい数字を選ぶ</small></div>')
s=s.replace('正解の道をえらんで ルートを進もう！','正しい数字をえらんで ルートを進もう！')
s=s.replace('<span>正解なら次の冒険ポイントへ進みます。</span>','<span>正解すると次の冒険ポイントへ進みます。</span>')
s=s.replace('数字を見て、進みたい道を選ぼう。','数字を見て、正しい数字を選ぼう。')
s=s.replace('正しい数字は1つ以上あるよ。','正しい数字を1つ選ぼう。')
s=s.replace('もう一度、4つの道から選んでみよう！','もう一度、4つの数字から選んでみよう！')
p.write_text(s)
print('updated index.html')