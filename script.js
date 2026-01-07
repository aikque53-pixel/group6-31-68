let allQuestions = []
let quiz = { questions: [], current: 0, score: 0, answers: [] }

function $(id){return document.getElementById(id)}

async function loadQuestions(){
  try{
    const res = await fetch('data/questions.json')
    if(!res.ok) throw new Error('HTTP ' + res.status)
    allQuestions = await res.json()
  }catch(err){
    console.error('Failed to load questions.json',err)
    // show friendly in-page banner and fall back to embedded questions so the game is playable
    showBanner('Unable to load questions from data/questions.json. Running fallback questions so the game is playable. To fix permanently, serve the folder over HTTP (see README).')
    allQuestions = FALLBACK_QUESTIONS.slice()
  }
}

// Small fallback question set used when `fetch` fails (keeps game playable from file://)
const FALLBACK_QUESTIONS = [
  {
    question: 'Who was the first emperor of Rome?',
    continent: 'Europe',
    region: 'Western Europe',
    difficulty: 'easy',
    choices: ['Julius Caesar','Augustus','Nero','Constantine'],
    answer: 'Augustus',
    noImage: true
  },
  {
    question: 'In which year did the Battle of Hastings take place?',
    continent: 'Europe',
    region: 'British Isles',
    difficulty: 'easy',
    choices: ['1066','1215','1415','1666'],
    answer: '1066',
    noImage: true
  },
  {
    question: 'Which empire built Machu Picchu?',
    continent: 'South America',
    region: 'Andes',
    difficulty: 'medium',
    choices: ['Aztec','Maya','Inca','Olmec'],
    answer: 'Inca',
    noImage: true
  }
]

function showBanner(msg){
  const b = $('banner')
  if(!b) return
  const msgEl = $('bannerMsg')
  const runBtn = $('runLocalBtn')
  const runPanel = $('runPanel')
  const copyBtn = $('copyCmdBtn')
  const cmdsEl = $('runCommands')
  msgEl.textContent = msg
  // show run button so user can reveal local-server commands
  if(runBtn) runBtn.style.display = 'inline-block'
  if(b) b.style.display = 'block'

  if(runBtn){
    runBtn.onclick = ()=>{
      if(!runPanel) return
      runPanel.style.display = runPanel.style.display === 'none' ? 'block' : 'none'
    }
  }
  if(copyBtn && cmdsEl){
    copyBtn.onclick = async ()=>{
      try{
        await navigator.clipboard.writeText(cmdsEl.textContent)
        copyBtn.textContent = 'Copied'
        setTimeout(()=>copyBtn.textContent = 'Copy commands',2000)
      }catch(e){
        // fallback: select the text for manual copy
        const range = document.createRange()
        range.selectNodeContents(cmdsEl)
        const sel = window.getSelection()
        sel.removeAllRanges()
        sel.addRange(range)
        alert('Commands selected — press Ctrl+C to copy')
      }
    }
  }
}

function getSelectedContinents(){
  return Array.from(document.querySelectorAll('.checkboxes input[type=checkbox]:checked')).map(i=>i.value)
}

function getSelectedDifficulty(){
  const r = document.querySelector('input[name="difficulty"]:checked')
  return r ? r.value : 'easy'
}

function shuffle(arr){
  for(let i=arr.length-1;i>0;i--){
    const j=Math.floor(Math.random()*(i+1));[arr[i],arr[j]]=[arr[j],arr[i]]
  }
}

function startQuiz(){
  const continents = getSelectedContinents()
  const diff = getSelectedDifficulty()
  const num = parseInt($('numQuestions').value,10)
  const filtered = allQuestions.filter(q=>continents.includes(q.continent) && q.difficulty===diff)
  if(filtered.length===0){alert('No questions match your selection. Try different filters.');return}
  shuffle(filtered)
  quiz.questions = filtered.slice(0,Math.min(num,filtered.length))
  quiz.current = 0
  quiz.score = 0
  quiz.answers = []
  $('controls').classList.add('hidden')
  $('results').classList.add('hidden')
  $('quiz').classList.remove('hidden')
  $('total').textContent = quiz.questions.length
  renderQuestion()
}

function renderQuestion(){
  const q = quiz.questions[quiz.current]
  $('current').textContent = quiz.current+1
  $('questionText').textContent = `${q.question} (${q.region} — ${q.continent})`
  // images removed
  const choicesDiv = $('choices')
  choicesDiv.innerHTML = ''
  const choices = q.choices.slice()
  shuffle(choices)
  for(const c of choices){
    const btn = document.createElement('div')
    btn.className = 'choice'
    btn.textContent = c
    btn.onclick = ()=>selectChoice(btn,c,q.answer)
    choicesDiv.appendChild(btn)
  }
  $('nextBtn').disabled = true
}

function selectChoice(elem,choice,correct){
  if($('nextBtn').disabled===false && quiz.current>=quiz.questions.length) return
  const children = Array.from(document.querySelectorAll('.choice'))
  children.forEach(ch=>ch.onclick=null)
  if(choice===correct){
    elem.classList.add('correct')
    quiz.score++
    quiz.answers.push({ok:true,choice,correct})
  } else {
    elem.classList.add('wrong')
    // mark correct one
    children.find(c=>c.textContent===correct)?.classList.add('correct')
    quiz.answers.push({ok:false,choice,correct})
  }
  $('nextBtn').disabled = false
}

function nextQuestion(){
  quiz.current++
  if(quiz.current>=quiz.questions.length){
    showResults()
  } else {
    renderQuestion()
  }
}

function showResults(){
  $('quiz').classList.add('hidden')
  $('results').classList.remove('hidden')
  const total = quiz.questions.length
  const correct = quiz.score
  const percent = Math.round((correct/total)*100)
  // breakdown by continent
  const breakdown = {}
  quiz.questions.forEach((q,i)=>{
    const cont = q.continent
    breakdown[cont] = breakdown[cont]||{total:0,correct:0}
    breakdown[cont].total++
    if(quiz.answers[i].ok) breakdown[cont].correct++
  })
  let html = `<p><strong>Score:</strong> ${correct} / ${total} (${percent}%)</p>`
  html += '<h3>By Continent</h3><ul>'
  for(const [c,v] of Object.entries(breakdown)){
    const p = Math.round((v.correct/v.total)*100)
    html += `<li>${c}: ${v.correct}/${v.total} (${p}%)</li>`
  }
  html += '</ul>'
  html += '<h3>Answers</h3><ol>'
  quiz.questions.forEach((q,i)=>{
    const a = quiz.answers[i]
    html += `<li>${q.question} — <strong>${a.ok? 'Correct':'Wrong'}</strong><br/>Your answer: ${a.choice} · Correct: ${a.correct}</li>`
  })
  html += '</ol>'
  $('summary').innerHTML = html
}

function restart(){
  $('controls').classList.remove('hidden')
  $('results').classList.add('hidden')
}

window.addEventListener('DOMContentLoaded', async ()=>{
  // disable Start until questions are loaded
  $('startBtn').disabled = true
  await loadQuestions()
  if(allQuestions.length>0){
    $('startBtn').disabled = false
  }
  $('startBtn').addEventListener('click', startQuiz)
  $('nextBtn').addEventListener('click', nextQuestion)
  $('restartBtn').addEventListener('click', restart)
})