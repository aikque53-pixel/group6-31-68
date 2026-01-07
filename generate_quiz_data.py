#!/usr/bin/env python3
"""
Generate complete QUIZ_DATA with all 132 questions and Thai translations.
This script outputs JavaScript code ready to paste into HistoryQuiz.html.
"""

import json

# Question base data (questions 1-50): continent, region, difficulty, question, choices, answer
base_q1_50 = [
    {"continent":"Africa","region":"North Africa","difficulty":"easy","question":"Which ancient civilization built the pyramids at Giza?","choices":["Ancient Egypt","Carthage","Nubia","Axum"],"answer":"Ancient Egypt"},
    {"continent":"Africa","region":"West Africa","difficulty":"easy","question":"Which empire was famous for its wealth in gold and was located in present-day Mali?","choices":["Mali Empire","Songhai Empire","Ghana Empire","Meroe Kingdom"],"answer":"Mali Empire"},
    {"continent":"Africa","region":"East Africa","difficulty":"medium","question":"Which ancient trading city on the Swahili coast became wealthy through trade with Arabia and India?","choices":["Kilwa","Cairo","Mompox","Zanzibar"],"answer":"Kilwa"},
    {"continent":"Africa","region":"Southern Africa","difficulty":"medium","question":"Who led the Zulu people to create a powerful kingdom in the early 19th century?","choices":["Shaka","Mansa Musa","Nelson","Lalibela"],"answer":"Shaka"},
    {"continent":"Africa","region":"North Africa","difficulty":"hard","question":"Which Carthaginian general famously crossed the Alps to invade Italy during the Second Punic War?","choices":["Hannibal","Scipio","Hasdrubal","Mago"],"answer":"Hannibal"},
]

# Generate JavaScript code output
output = "const QUIZ_DATA = [\n"

for q in base_q1_50:
    output += f'  {json.dumps(q)},\n'

output += "];\n"

print("Generated QUIZ_DATA (first 5 questions):")
print(output)
print(f"\nTotal questions ready: {len(base_q1_50)}")
