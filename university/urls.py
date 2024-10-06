from django.urls import path
from .views import (
    FacultyList, FacultyDetail, GroupList, GroupDetail,
    DepartmentList, DepartmentDetail, SubjectList, SubjectDetail,
    TeacherList, TeacherDetail, StudentList, StudentDetail
)

urlpatterns = [
    path('faculties/', FacultyList.as_view(), name='faculties'),
    path('faculties/<int:pk>/', FacultyDetail.as_view(), name='faculty_detail'),
    path('groups/', GroupList.as_view(), name='groups'),
    path('groups/<int:pk>/', GroupDetail.as_view(), name='group_detail'),
    path('departments/', DepartmentList.as_view(), name='departments'),
    path('departments/<int:pk>/', DepartmentDetail.as_view(), name='department_detail'),
    path('subjects/', SubjectList.as_view(), name='subjects'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject_detail'),
    path('teachers/', TeacherList.as_view(), name='teachers'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher_detail'),
    path('students/', StudentList.as_view(), name='students'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
]