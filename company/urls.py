from rest_framework.routers import DefaultRouter
from company.views import EmployeeAPIViewSet, ProgrammingLanguageAPIViewSet, DepartmentAPIViewSet

router = DefaultRouter()
router.register('employee', EmployeeAPIViewSet, basename='Employee')
router.register('department', ProgrammingLanguageAPIViewSet, basename='Programming_Language')
router.register('programming_languages', DepartmentAPIViewSet, basename='Department')

urlpatterns = router.urls
