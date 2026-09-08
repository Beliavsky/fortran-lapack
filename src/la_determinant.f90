!> Determinant of a rectangular matrix
module la_determinant
     use la_constants
     use la_blas
     use la_lapack
     use la_state_type
     use iso_fortran_env,only:real32,real64,real128,int8,int16,int32,int64,stderr => error_unit
     implicit none(type,external)
     private

     public :: det,determinant_into

     character(*),parameter :: this = 'determinant'

     !> @brief Compute the determinant of a rectangular matrix.
     !!
     !! This function computes the determinant of a real or complex rectangular matrix \f$ A \f$.
     !! The determinant is calculated using LU factorization.
     !!
     !! @param[in,out] A The input square matrix of size \f$ [m, n] \f$. If `overwrite_a` is true,
     !!                  the contents of A may be modified during computation.
     !! @param[in] overwrite_a (Optional) If `.true.`, A may be overwritten and destroyed. Default is `.false.`.
     !! @param[out] err (Optional) A state return flag. If an error occurs and `err` is not provided,
     !!                 the function will stop execution.
     !!
     !! @return The determinant of the matrix \f$ A \f$. The result is a `real` scalar value of the same
     !!         kind as the input matrix.
     !!
     !! @note This function relies on a matrix factorization approach (e.g., LU decomposition) to compute
     !!       the determinant efficiently from the [getrf](@ref la_lapack::getrf) backend.
     !! @warning If `overwrite_a` is enabled, the original contents of A will be lost.
     !!
     interface det
        module procedure la_sdeterminant
        module procedure la_ddeterminant
        module procedure la_qdeterminant
        module procedure la_cdeterminant
        module procedure la_zdeterminant
        module procedure la_wdeterminant
     end interface det

     !> @brief Compute a determinant through a pure subroutine interface.
     !!
     !! This interface leaves the input matrix unchanged, returns the determinant
     !! through `value`, and reports failures through the optional state argument.
     interface determinant_into
        module procedure la_sdeterminant_into
        module procedure la_ddeterminant_into
        module procedure la_qdeterminant_into
        module procedure la_cdeterminant_into
        module procedure la_zdeterminant_into
        module procedure la_wdeterminant_into
     end interface determinant_into

     !> @brief Compute the determinant of a square matrix using the `.det.` operator.
     !!
     !! This operator computes the determinant of a real or complex square matrix \f$ A \f$
     !! from its LU factorization, in a `pure` context and without an error flag.
     !!
     !! @param[in] A The input square matrix of size \f$ [n, n] \f$.
     !!
     !! @return The determinant of the matrix \f$ A \f$, of the same kind as \f$ A \f$.
     !!
     !! @note This operator is a shorthand for the `pure` determinant, allowing expressions such as:
     !!       \f$ d = .det. A \f$
     !! @warning The matrix \f$ A \f$ is copied internally, so the operator never modifies its argument.
     !!          Execution stops if the matrix is not square.
     !!
     public :: operator(.det.)

     ! Operator interface
     interface operator(.det.)
        module procedure la_spure_determinant
        module procedure la_dpure_determinant
        module procedure la_qpure_determinant
        module procedure la_cpure_determinant
        module procedure la_zpure_determinant
        module procedure la_wpure_determinant
     end interface operator(.det.)

     contains

     !> Compute a determinant without modifying the input matrix.
     pure subroutine la_sdeterminant_into(a,value,err)
         real(sp),intent(in) :: a(:,:) !! Input square matrix.
         real(sp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         real(sp),allocatable :: work(:,:)

         allocate (work,source=a)
         call la_sdeterminant_inplace(work,value,err)

     end subroutine la_sdeterminant_into

     !> Compute a determinant while using the input matrix as workspace.
     pure subroutine la_sdeterminant_inplace(a,value,err)
         real(sp),intent(inout) :: a(:,:) !! Input matrix, overwritten during factorization.
         real(sp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         type(la_state) :: err0
         integer(ilp) :: m,n,info,perm,k
         integer(ilp),allocatable :: ipiv(:)

         m = size(a,1,kind=ilp)
         n = size(a,2,kind=ilp)
         value = 0.0_sp

         if (m /= n) then
            err0 = la_state(this,LINALG_VALUE_ERROR,'invalid or non-square matrix: a=[',m,',',n,']')
            call err0%handle(err)
            return
         end if

         select case (m)
            case (0)
                value = 1.0_sp
            case (1)
                value = a(1,1)
            case default
                allocate (ipiv(n))
                call getrf(m,n,a,m,ipiv,info)

                select case (info)
                   case (0)
                       value = 1.0_sp
                       perm = 0
                       do k = 1,n
                          if (ipiv(k) /= k) perm = perm + 1
                          value = value*a(k,k)
                       end do
                       if (mod(perm,2) /= 0) value = -value
                   case (:-1)
                       err0 = la_state(this,LINALG_ERROR,'invalid matrix size a=[',m,',',n,']')
                   case (1:)
                       err0 = la_state(this,LINALG_ERROR,'singular matrix')
                   case default
                       err0 = la_state(this,LINALG_INTERNAL_ERROR,'catastrophic error')
                end select
         end select

         call err0%handle(err)

     end subroutine la_sdeterminant_inplace

     !> Compute determinant of a square matrix A.
     function la_sdeterminant(a,overwrite_a,err) result(det)
         !> Input matrix a[m,n]
         real(sp),intent(inout),target :: a(:,:)
         !> [optional] Can A data be overwritten and destroyed?
         logical(lk),optional,intent(in) :: overwrite_a
         !> [optional] state return flag. On error if not requested, the code will stop
         type(la_state),optional,intent(out) :: err
         !> Result: matrix determinant
         real(sp) :: det

         logical(lk) :: copy_a

         ! Can A be overwritten? By default, do not overwrite
         if (present(overwrite_a)) then
            copy_a = .not. overwrite_a
         else
            copy_a = .true._lk
         end if

         if (copy_a) then
            call la_sdeterminant_into(a,det,err)
         else
            call la_sdeterminant_inplace(a,det,err)
         end if

     end function la_sdeterminant

     ! Compute determinant of a square matrix A, without error control
     pure function la_spure_determinant(a) result(det)
         !> Input matrix a[m,n]
         real(sp),intent(in) :: a(:,:)
         !> Result: matrix determinant
         real(sp) :: det

         type(la_state) :: err0

         call la_sdeterminant_into(a,det,err0)
         call err0%handle()

     end function la_spure_determinant

     !> Compute a determinant without modifying the input matrix.
     pure subroutine la_ddeterminant_into(a,value,err)
         real(dp),intent(in) :: a(:,:) !! Input square matrix.
         real(dp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         real(dp),allocatable :: work(:,:)

         allocate (work,source=a)
         call la_ddeterminant_inplace(work,value,err)

     end subroutine la_ddeterminant_into

     !> Compute a determinant while using the input matrix as workspace.
     pure subroutine la_ddeterminant_inplace(a,value,err)
         real(dp),intent(inout) :: a(:,:) !! Input matrix, overwritten during factorization.
         real(dp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         type(la_state) :: err0
         integer(ilp) :: m,n,info,perm,k
         integer(ilp),allocatable :: ipiv(:)

         m = size(a,1,kind=ilp)
         n = size(a,2,kind=ilp)
         value = 0.0_dp

         if (m /= n) then
            err0 = la_state(this,LINALG_VALUE_ERROR,'invalid or non-square matrix: a=[',m,',',n,']')
            call err0%handle(err)
            return
         end if

         select case (m)
            case (0)
                value = 1.0_dp
            case (1)
                value = a(1,1)
            case default
                allocate (ipiv(n))
                call getrf(m,n,a,m,ipiv,info)

                select case (info)
                   case (0)
                       value = 1.0_dp
                       perm = 0
                       do k = 1,n
                          if (ipiv(k) /= k) perm = perm + 1
                          value = value*a(k,k)
                       end do
                       if (mod(perm,2) /= 0) value = -value
                   case (:-1)
                       err0 = la_state(this,LINALG_ERROR,'invalid matrix size a=[',m,',',n,']')
                   case (1:)
                       err0 = la_state(this,LINALG_ERROR,'singular matrix')
                   case default
                       err0 = la_state(this,LINALG_INTERNAL_ERROR,'catastrophic error')
                end select
         end select

         call err0%handle(err)

     end subroutine la_ddeterminant_inplace

     !> Compute determinant of a square matrix A.
     function la_ddeterminant(a,overwrite_a,err) result(det)
         !> Input matrix a[m,n]
         real(dp),intent(inout),target :: a(:,:)
         !> [optional] Can A data be overwritten and destroyed?
         logical(lk),optional,intent(in) :: overwrite_a
         !> [optional] state return flag. On error if not requested, the code will stop
         type(la_state),optional,intent(out) :: err
         !> Result: matrix determinant
         real(dp) :: det

         logical(lk) :: copy_a

         ! Can A be overwritten? By default, do not overwrite
         if (present(overwrite_a)) then
            copy_a = .not. overwrite_a
         else
            copy_a = .true._lk
         end if

         if (copy_a) then
            call la_ddeterminant_into(a,det,err)
         else
            call la_ddeterminant_inplace(a,det,err)
         end if

     end function la_ddeterminant

     ! Compute determinant of a square matrix A, without error control
     pure function la_dpure_determinant(a) result(det)
         !> Input matrix a[m,n]
         real(dp),intent(in) :: a(:,:)
         !> Result: matrix determinant
         real(dp) :: det

         type(la_state) :: err0

         call la_ddeterminant_into(a,det,err0)
         call err0%handle()

     end function la_dpure_determinant

     !> Compute a determinant without modifying the input matrix.
     pure subroutine la_qdeterminant_into(a,value,err)
         real(qp),intent(in) :: a(:,:) !! Input square matrix.
         real(qp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         real(qp),allocatable :: work(:,:)

         allocate (work,source=a)
         call la_qdeterminant_inplace(work,value,err)

     end subroutine la_qdeterminant_into

     !> Compute a determinant while using the input matrix as workspace.
     pure subroutine la_qdeterminant_inplace(a,value,err)
         real(qp),intent(inout) :: a(:,:) !! Input matrix, overwritten during factorization.
         real(qp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         type(la_state) :: err0
         integer(ilp) :: m,n,info,perm,k
         integer(ilp),allocatable :: ipiv(:)

         m = size(a,1,kind=ilp)
         n = size(a,2,kind=ilp)
         value = 0.0_qp

         if (m /= n) then
            err0 = la_state(this,LINALG_VALUE_ERROR,'invalid or non-square matrix: a=[',m,',',n,']')
            call err0%handle(err)
            return
         end if

         select case (m)
            case (0)
                value = 1.0_qp
            case (1)
                value = a(1,1)
            case default
                allocate (ipiv(n))
                call getrf(m,n,a,m,ipiv,info)

                select case (info)
                   case (0)
                       value = 1.0_qp
                       perm = 0
                       do k = 1,n
                          if (ipiv(k) /= k) perm = perm + 1
                          value = value*a(k,k)
                       end do
                       if (mod(perm,2) /= 0) value = -value
                   case (:-1)
                       err0 = la_state(this,LINALG_ERROR,'invalid matrix size a=[',m,',',n,']')
                   case (1:)
                       err0 = la_state(this,LINALG_ERROR,'singular matrix')
                   case default
                       err0 = la_state(this,LINALG_INTERNAL_ERROR,'catastrophic error')
                end select
         end select

         call err0%handle(err)

     end subroutine la_qdeterminant_inplace

     !> Compute determinant of a square matrix A.
     function la_qdeterminant(a,overwrite_a,err) result(det)
         !> Input matrix a[m,n]
         real(qp),intent(inout),target :: a(:,:)
         !> [optional] Can A data be overwritten and destroyed?
         logical(lk),optional,intent(in) :: overwrite_a
         !> [optional] state return flag. On error if not requested, the code will stop
         type(la_state),optional,intent(out) :: err
         !> Result: matrix determinant
         real(qp) :: det

         logical(lk) :: copy_a

         ! Can A be overwritten? By default, do not overwrite
         if (present(overwrite_a)) then
            copy_a = .not. overwrite_a
         else
            copy_a = .true._lk
         end if

         if (copy_a) then
            call la_qdeterminant_into(a,det,err)
         else
            call la_qdeterminant_inplace(a,det,err)
         end if

     end function la_qdeterminant

     ! Compute determinant of a square matrix A, without error control
     pure function la_qpure_determinant(a) result(det)
         !> Input matrix a[m,n]
         real(qp),intent(in) :: a(:,:)
         !> Result: matrix determinant
         real(qp) :: det

         type(la_state) :: err0

         call la_qdeterminant_into(a,det,err0)
         call err0%handle()

     end function la_qpure_determinant

     !> Compute a determinant without modifying the input matrix.
     pure subroutine la_cdeterminant_into(a,value,err)
         complex(sp),intent(in) :: a(:,:) !! Input square matrix.
         complex(sp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         complex(sp),allocatable :: work(:,:)

         allocate (work,source=a)
         call la_cdeterminant_inplace(work,value,err)

     end subroutine la_cdeterminant_into

     !> Compute a determinant while using the input matrix as workspace.
     pure subroutine la_cdeterminant_inplace(a,value,err)
         complex(sp),intent(inout) :: a(:,:) !! Input matrix, overwritten during factorization.
         complex(sp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         type(la_state) :: err0
         integer(ilp) :: m,n,info,perm,k
         integer(ilp),allocatable :: ipiv(:)

         m = size(a,1,kind=ilp)
         n = size(a,2,kind=ilp)
         value = 0.0_sp

         if (m /= n) then
            err0 = la_state(this,LINALG_VALUE_ERROR,'invalid or non-square matrix: a=[',m,',',n,']')
            call err0%handle(err)
            return
         end if

         select case (m)
            case (0)
                value = 1.0_sp
            case (1)
                value = a(1,1)
            case default
                allocate (ipiv(n))
                call getrf(m,n,a,m,ipiv,info)

                select case (info)
                   case (0)
                       value = 1.0_sp
                       perm = 0
                       do k = 1,n
                          if (ipiv(k) /= k) perm = perm + 1
                          value = value*a(k,k)
                       end do
                       if (mod(perm,2) /= 0) value = -value
                   case (:-1)
                       err0 = la_state(this,LINALG_ERROR,'invalid matrix size a=[',m,',',n,']')
                   case (1:)
                       err0 = la_state(this,LINALG_ERROR,'singular matrix')
                   case default
                       err0 = la_state(this,LINALG_INTERNAL_ERROR,'catastrophic error')
                end select
         end select

         call err0%handle(err)

     end subroutine la_cdeterminant_inplace

     !> Compute determinant of a square matrix A.
     function la_cdeterminant(a,overwrite_a,err) result(det)
         !> Input matrix a[m,n]
         complex(sp),intent(inout),target :: a(:,:)
         !> [optional] Can A data be overwritten and destroyed?
         logical(lk),optional,intent(in) :: overwrite_a
         !> [optional] state return flag. On error if not requested, the code will stop
         type(la_state),optional,intent(out) :: err
         !> Result: matrix determinant
         complex(sp) :: det

         logical(lk) :: copy_a

         ! Can A be overwritten? By default, do not overwrite
         if (present(overwrite_a)) then
            copy_a = .not. overwrite_a
         else
            copy_a = .true._lk
         end if

         if (copy_a) then
            call la_cdeterminant_into(a,det,err)
         else
            call la_cdeterminant_inplace(a,det,err)
         end if

     end function la_cdeterminant

     ! Compute determinant of a square matrix A, without error control
     pure function la_cpure_determinant(a) result(det)
         !> Input matrix a[m,n]
         complex(sp),intent(in) :: a(:,:)
         !> Result: matrix determinant
         complex(sp) :: det

         type(la_state) :: err0

         call la_cdeterminant_into(a,det,err0)
         call err0%handle()

     end function la_cpure_determinant

     !> Compute a determinant without modifying the input matrix.
     pure subroutine la_zdeterminant_into(a,value,err)
         complex(dp),intent(in) :: a(:,:) !! Input square matrix.
         complex(dp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         complex(dp),allocatable :: work(:,:)

         allocate (work,source=a)
         call la_zdeterminant_inplace(work,value,err)

     end subroutine la_zdeterminant_into

     !> Compute a determinant while using the input matrix as workspace.
     pure subroutine la_zdeterminant_inplace(a,value,err)
         complex(dp),intent(inout) :: a(:,:) !! Input matrix, overwritten during factorization.
         complex(dp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         type(la_state) :: err0
         integer(ilp) :: m,n,info,perm,k
         integer(ilp),allocatable :: ipiv(:)

         m = size(a,1,kind=ilp)
         n = size(a,2,kind=ilp)
         value = 0.0_dp

         if (m /= n) then
            err0 = la_state(this,LINALG_VALUE_ERROR,'invalid or non-square matrix: a=[',m,',',n,']')
            call err0%handle(err)
            return
         end if

         select case (m)
            case (0)
                value = 1.0_dp
            case (1)
                value = a(1,1)
            case default
                allocate (ipiv(n))
                call getrf(m,n,a,m,ipiv,info)

                select case (info)
                   case (0)
                       value = 1.0_dp
                       perm = 0
                       do k = 1,n
                          if (ipiv(k) /= k) perm = perm + 1
                          value = value*a(k,k)
                       end do
                       if (mod(perm,2) /= 0) value = -value
                   case (:-1)
                       err0 = la_state(this,LINALG_ERROR,'invalid matrix size a=[',m,',',n,']')
                   case (1:)
                       err0 = la_state(this,LINALG_ERROR,'singular matrix')
                   case default
                       err0 = la_state(this,LINALG_INTERNAL_ERROR,'catastrophic error')
                end select
         end select

         call err0%handle(err)

     end subroutine la_zdeterminant_inplace

     !> Compute determinant of a square matrix A.
     function la_zdeterminant(a,overwrite_a,err) result(det)
         !> Input matrix a[m,n]
         complex(dp),intent(inout),target :: a(:,:)
         !> [optional] Can A data be overwritten and destroyed?
         logical(lk),optional,intent(in) :: overwrite_a
         !> [optional] state return flag. On error if not requested, the code will stop
         type(la_state),optional,intent(out) :: err
         !> Result: matrix determinant
         complex(dp) :: det

         logical(lk) :: copy_a

         ! Can A be overwritten? By default, do not overwrite
         if (present(overwrite_a)) then
            copy_a = .not. overwrite_a
         else
            copy_a = .true._lk
         end if

         if (copy_a) then
            call la_zdeterminant_into(a,det,err)
         else
            call la_zdeterminant_inplace(a,det,err)
         end if

     end function la_zdeterminant

     ! Compute determinant of a square matrix A, without error control
     pure function la_zpure_determinant(a) result(det)
         !> Input matrix a[m,n]
         complex(dp),intent(in) :: a(:,:)
         !> Result: matrix determinant
         complex(dp) :: det

         type(la_state) :: err0

         call la_zdeterminant_into(a,det,err0)
         call err0%handle()

     end function la_zpure_determinant

     !> Compute a determinant without modifying the input matrix.
     pure subroutine la_wdeterminant_into(a,value,err)
         complex(qp),intent(in) :: a(:,:) !! Input square matrix.
         complex(qp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         complex(qp),allocatable :: work(:,:)

         allocate (work,source=a)
         call la_wdeterminant_inplace(work,value,err)

     end subroutine la_wdeterminant_into

     !> Compute a determinant while using the input matrix as workspace.
     pure subroutine la_wdeterminant_inplace(a,value,err)
         complex(qp),intent(inout) :: a(:,:) !! Input matrix, overwritten during factorization.
         complex(qp),intent(out) :: value !! Computed determinant.
         type(la_state),optional,intent(out) :: err !! Error status.

         type(la_state) :: err0
         integer(ilp) :: m,n,info,perm,k
         integer(ilp),allocatable :: ipiv(:)

         m = size(a,1,kind=ilp)
         n = size(a,2,kind=ilp)
         value = 0.0_qp

         if (m /= n) then
            err0 = la_state(this,LINALG_VALUE_ERROR,'invalid or non-square matrix: a=[',m,',',n,']')
            call err0%handle(err)
            return
         end if

         select case (m)
            case (0)
                value = 1.0_qp
            case (1)
                value = a(1,1)
            case default
                allocate (ipiv(n))
                call getrf(m,n,a,m,ipiv,info)

                select case (info)
                   case (0)
                       value = 1.0_qp
                       perm = 0
                       do k = 1,n
                          if (ipiv(k) /= k) perm = perm + 1
                          value = value*a(k,k)
                       end do
                       if (mod(perm,2) /= 0) value = -value
                   case (:-1)
                       err0 = la_state(this,LINALG_ERROR,'invalid matrix size a=[',m,',',n,']')
                   case (1:)
                       err0 = la_state(this,LINALG_ERROR,'singular matrix')
                   case default
                       err0 = la_state(this,LINALG_INTERNAL_ERROR,'catastrophic error')
                end select
         end select

         call err0%handle(err)

     end subroutine la_wdeterminant_inplace

     !> Compute determinant of a square matrix A.
     function la_wdeterminant(a,overwrite_a,err) result(det)
         !> Input matrix a[m,n]
         complex(qp),intent(inout),target :: a(:,:)
         !> [optional] Can A data be overwritten and destroyed?
         logical(lk),optional,intent(in) :: overwrite_a
         !> [optional] state return flag. On error if not requested, the code will stop
         type(la_state),optional,intent(out) :: err
         !> Result: matrix determinant
         complex(qp) :: det

         logical(lk) :: copy_a

         ! Can A be overwritten? By default, do not overwrite
         if (present(overwrite_a)) then
            copy_a = .not. overwrite_a
         else
            copy_a = .true._lk
         end if

         if (copy_a) then
            call la_wdeterminant_into(a,det,err)
         else
            call la_wdeterminant_inplace(a,det,err)
         end if

     end function la_wdeterminant

     ! Compute determinant of a square matrix A, without error control
     pure function la_wpure_determinant(a) result(det)
         !> Input matrix a[m,n]
         complex(qp),intent(in) :: a(:,:)
         !> Result: matrix determinant
         complex(qp) :: det

         type(la_state) :: err0

         call la_wdeterminant_into(a,det,err0)
         call err0%handle()

     end function la_wpure_determinant

end module la_determinant
