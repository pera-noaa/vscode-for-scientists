program calibration_demo
   use calibration_mod
   implicit none

   type(calib_coef_t) :: coef
   real(kind=8) :: raw_values(5)
   real(kind=8) :: calibrated(5)
   real(kind=8) :: mean_val, min_val, max_val
   integer :: i, n

   coef = calib_coef_t(slope=1.02d0, offset=-0.15d0)
   raw_values = [10.0d0, 12.0d0, 11.5d0, 9.8d0, 10.7d0]
   n = size(raw_values)

   do i = 1, n
      calibrated(i) = apply_calibration(raw_values(i), coef)
   end do

   call calibration_summary(calibrated, n, mean_val, min_val, max_val)

   print *, 'Calibrated mean:', mean_val
   print *, '         min:  ', min_val
   print *, '         max:  ', max_val

end program calibration_demo
