dict1 = {
    "A":[20,30,100,49],
    "B":[00,199,201,29],
    "C":[40,90,69,18]
}

max_res = 0
for sub, vals in dict1.items():
      
    # storing maximum of difference
    max_res = max(max_res, max(vals) - min(vals))    
    if max_res == max(vals) - min(vals):
        res = sub
          
# printing result 
print("The maximum element key : " + str(res)) 