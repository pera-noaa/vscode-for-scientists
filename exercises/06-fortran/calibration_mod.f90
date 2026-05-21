module calibration_mod
   implicit none
   private
   public :: apply_calibration, calibration_summary, calib_coef_t

   type :: calib_coef_t
      real(kind=8) :: slope
      real(kind=8) :: offset
   end type calib_coef_t

contains

   function apply_calibration(raw, coef) result(calibrated)
      ! Linear calibration: y = slope * x + offset.
      real(kind=8), intent(in) :: raw
      type(calib_coef_t), intent(in) :: coef
      real(kind=8) :: calibrated

      calibrated = coef%slope * raw + coef%offset
   end function apply_calibration

   subroutine calibration_summary(values, n, mean_out, min_out, max_out)
      ! Mean, min, max of the first `n` entries of `values`.
      real(kind=8), intent(in) :: values(:)
      integer, intent(in) :: n
      real(kind=8), intent(out) :: mean_out
      real(kind=8), intent(out) :: min_out
      real(kind=8), intent(out) :: max_out

      integer :: i

      mean_out = 0.0d0
      min_out = values(1)
      max_out = values(1)

      do i = 1, n
         mean_out = mean_out + values(i)
         if (values(i) < min_out) min_out = values(i)
         if (values(i) > max_out) max_out = values(i)
      end do

      mean_out = mean_out / real(n, kind=8)
   end subroutine calibration_summary

end module calibration_mod
