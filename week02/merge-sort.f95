program MergeSort 
   implicit none
   integer, parameter :: N = 10
   integer :: A(N) = (/10, 11, 12, 13, 14, 5, 4, 3, 2, 1/)
   integer, dimension ((n + 1)/2) :: D 
   write(*,*)'Unsorted array :', A
   call RecMergeSort(A, N, D)
   write(*,*)'Sorted array:', A 
contains
   
subroutine merge(A, B, C)
    implicit none
    
    integer, intent(in) :: A(:), B(:)
    integer, intent(inout) :: C(:)
    integer :: i, j, k 
    
    i = 1; j = 1; k = 1;
    do while (i <= size(A) .and. j <= size(B))
       if (A(i) <= B(j)) then
          C(k) = A(i)
          i = i + 1 
        else 
          C(k) = B(j)
          j = j + 1 
        end if
        k = k + 1 
    enddo 
    do while (i <= size(A))
       C(k) = A(i)
       i = i + 1 
       k = k + 1 
    enddo
    return
end subroutine merge

recursive subroutine RecMergeSort(A, N, D)
   implicit none
   
   integer, intent(in) :: N
   integer, dimension(N), intent(inout) :: A 
   integer, dimension((N + 1)/2), intent(out) :: D 
   
   integer :: mid, tmp
   
   if (N < 2) return
   if (N == 2) then 
       if (A(1) > A(2)) then 
           tmp = A(1)
           A(1) = A(2)
           A(2) = tmp
        endif
        return
    endif
    mid = (N + 1)/2
    
    
    call RecMergeSort(A, mid, D)
    call RecMergeSort(A(mid+1), N-mid, D)
    
    if (A(mid) > A(mid + 1)) then
        D(1:mid) = A(1:mid)
        call merge(D(1:mid), A(mid+1:),A)
    endif
    return
end subroutine RecMergeSort
end program MergeSort

