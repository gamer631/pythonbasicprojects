"""Small multiple-choice Python quiz."""
QUESTIONS=[('Which keyword creates a function?',['for','def','class','return'],'b'),('Which type stores key/value pairs?',['list','tuple','dict','set'],'c'),('What does len("cat") return?',['2','3','4','cat'],'b')]
def main():
    score=0
    for i,(question,choices,answer) in enumerate(QUESTIONS,1):
        print(f'\n{i}. {question}')
        for label,choice in zip('abcd',choices): print(f' {label}) {choice}')
        if input('Answer: ').strip().lower()==answer: print('Correct!'); score+=1
        else: print(f'Answer: {answer}')
    print(f'Final score: {score}/{len(QUESTIONS)}')
if __name__=='__main__': main()
