def balanced_arr(arr):
   run_even_sum=0
   run_odd_sum=0
   odd_sum=0
   even_sum=0
   l=list()
   for i in range(len(arr)):
     if i%2==0:
        even_sum+=arr[i]
     elif i%2!=0:
        odd_sum+=arr[i]
   for i in range(len(arr)):
      if i%2==0:
        if (even_sum-run_even_sum-arr[i]+run_odd_sum)==(run_even_sum+odd_sum-run_odd_sum):
           l.append(i)
        run_even_sum+=arr[i]
      elif i%2!=0:
        if (even_sum-run_even_sum+run_odd_sum)==(run_even_sum+odd_sum-arr[i]+run_odd_sum):
           l.append(i)
        run_odd_sum+=arr[i]
   return len(l)

if __name__=="__main__":
   print(balanced_arr([2, 1, 6, 4]))
   print(balanced_arr([5, 5, 2, 5, 8]))
   