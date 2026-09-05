from pathlib import Path
p = Path('index.html')
s = p.read_text()
old = """function choices(){const dirs=['U','R','D','L'],correctDir=state.route[state.step+1].dir;\n  const correctIndex=dirs.indexOf(correctDir);\n  const used=new Set(),vals=Array(4);\n  const correct=getCorrectValue();\n  vals[correctIndex]=correct;used.add(correct);\n  for(let i=0;i<4;i++){\n    if(i===correctIndex)continue;\n    const d=getDistractor(used);used.add(d);vals[i]=d;\n  }\n  state.sceneCorrect=correct;\n  return dirs.map((dir,i)=>({dir,value:vals[i],ok:i===correctIndex}));\n}"""
new = """function choices(){\n  const dirs=['U','R','D','L'];\n  const used=new Set(),vals=Array(4);\n  const correct=getCorrectValue();\n  const correctIndex=rnd(0,3);\n  vals[correctIndex]=correct;used.add(correct);\n  for(let i=0;i<4;i++){\n    if(i===correctIndex)continue;\n    const d=getDistractor(used);used.add(d);vals[i]=d;\n  }\n  state.sceneCorrect=correct;\n  return dirs.map((dir,i)=>({dir,value:vals[i],ok:i===correctIndex}));\n}"""
if old not in s:
    raise SystemExit('target choices() block not found')
s=s.replace(old,new)
repls={
'4つの数字から、条件に合う道を見つけよう。正解するたびに、ナビキャラと冒険ルートが先へ進むよ。':'4つの数字から、条件に合う数字を見つけよう。正解するたびに、ナビキャラと冒険ルートが先へ進むよ。',
'<div class="card"><b>4方向</b><small>上・右・下・左</small></div>':'<div class="card"><b>4択</b><small>正しい数字を選ぶ</small></div>',
'正解の道をえらんで ルートを進もう！':'正しい数字をえらんで ルートを進もう！',
'<span>正解なら次の冒険ポイントへ進みます。</span>':'<span>正解すると次の冒険ポイントへ進みます。</span>',
'数字を見て、進みたい道を選ぼう。':'数字を見て、正しい数字を選ぼう。',
'正しい数字は1つ以上あるよ。':'正しい数字を1つ選ぼう。',
'もう一度、4つの道から選んでみよう！':'もう一度、4つの数字から選んでみよう！'}
for a,b in repls.items(): s=s.replace(a,b)
p.write_text(s)
print('updated index.html')
