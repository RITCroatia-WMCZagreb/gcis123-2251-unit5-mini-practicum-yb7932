import difflib
import pytest

from pi_tester import pi_tester
from pi_tester import display_score

def test_pi_tester_RES_1(capsys, monkeypatch, printFeedback=True):

    inputs = iter(["1","2"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   
    # Execute the function
      # Run the main function
    result = pi_tester()
    #Get the feedback
    captured = capsys.readouterr()

    assert result==1


def test_pi_tester_RES_2(capsys, monkeypatch, printFeedback=True):

    inputs = iter(["1","4","1","5","5"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   
    # Execute the function
      # Run the main function
    result = pi_tester()
    #Get the feedback
    captured = capsys.readouterr()

    assert result==4


def test_pi_tester_RES_3(capsys, monkeypatch, printFeedback=True):

    inputs = iter(["1","4","1","5","9","2","6","5","3","5","8","9","1"])


    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   
    # Execute the function
      # Run the main function
    result = pi_tester()
    #Get the feedback
    captured = capsys.readouterr()

    assert result==12


def test_display_score_pi_neophyte(capsys,monkeypatch,printFeedback=True):
    score = 3
    display_score(score)
    captured = capsys.readouterr()
    assert "PI Neophyte" in captured.out


def test_display_score_pi_novice(capsys, monkeypatch,printFeedback=True):
    score = 9
    display_score(score)
    captured = capsys.readouterr()
    assert "PI Novice" in captured.out, "The output does not contain the \"PI Novice\""


def test_display_score_pi_expert(capsys,monkeypatch,printFeedback=True):
    score = 100
    display_score(score)
    captured = capsys.readouterr()
    assert "PI Expert" in captured.out, "The output does not contain the \"PI Expert\""


def test_FinalGrade(capsys, monkeypatch):
    
    totalPoints = 0

    ## CALL the testers, do not print, otherwise you will mess with some of the testers
  
    test_functions = [
        (test_pi_tester_RES_1,20),
        (test_pi_tester_RES_2, 25),
        (test_pi_tester_RES_3, 25),
        (test_display_score_pi_neophyte,10),
        (test_display_score_pi_novice,10),
        (test_display_score_pi_expert,10)
    ]
     

    outputFeedbac = "############ TOTAL POINTS ###################\n"
    
    for function, point in test_functions:
            try:
                function(capsys,monkeypatch,False)
                outputFeedbac=outputFeedbac+f"PASS:{function.__name__}: {point}"+"\n"
                totalPoints += point
            except AssertionError:
                outputFeedbac=outputFeedbac+f"FAIL:{function.__name__}: {0}\n"
    
    print(outputFeedbac)
    print("Total points",totalPoints)
    assert True