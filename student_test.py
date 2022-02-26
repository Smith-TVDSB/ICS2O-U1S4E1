import pytest
import student 


def test_jump():
    try:
        input_values=['jump']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
    
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert output[1]=='jumping'

    except:
        input_values=['jump']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        student.input = mock_input
        student.print = lambda s,t : output.extend([s,t])

        student.main()

        assert output[1]+output[2][-3:]=='jumping'

def test_eat():
    try:
        input_values=['eat']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert output[1]=='eating' 
    
    except:
        input_values=['eat']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        student.input = mock_input
        student.print = lambda s,t : output.extend([s,t])

        student.main()

        assert output[1]+output[2][-3:]=='eating'   

def test_scarps():
    try:
        input_values=['scarp']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert output[1]=='scarping'

    except:
        input_values=['scarp']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        student.input = mock_input
        student.print = lambda s,t : output.extend([s,t])

        student.main()

        assert output[1]+output[2][-3:]=='scarping'

def test_groundbreak():
    try:
        input_values=['groundbreak']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert output[1]=='groundbreaking'
    except:
        input_values=['groundbreak']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        student.input = mock_input
        student.print = lambda s,t : output.extend([s,t])

        student.main()

        assert output[1]+output[2][-3:]=='groundbreaking'

