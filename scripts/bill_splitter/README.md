# Bill Splitter

> Python script to split bills equally

## Introduction

Imagine you go to a restaurant with four of your friends. The bill will be $105. You give $50 and others chip in $40, $10 and $5 and another friend dont have change so he didn't give. Bill should have been split $21 each way so now you need to calculate who owes howmuch to whom. This python script will solve this problem. The script takes contributions (individual share) to a bill and then gives who owes how much to whom with minimum number of transaction

## Usage

Run the script.py

```bash
cd bill_splitter
python script.py
```

Enter the number of people among whom the bill is supposed to be split. eg: `2`

```
Number of participants : 2
```

Enter the name of participant and his/her contribution to the bill separated by a space. eg: `John 50`

```
Enter name and contribution of participant 1 :
John 50
Enter name and contribution of participant 2 :
Travis 100
```

Output

```
John paid    $50
Travis paid    $100
--------------------------------
Total pool amount  : $150
Per head           : $75.0
--------------------------------
John should pay $25.0 to Travis
--------------------------------
```

## Conclusion

The algorithm is designed in such a way that it will generate a result that has least number of transaction involved to achieve maximum efficiency.

## Author : Samartha | [@yunghog](https://github.com/yunghog)
