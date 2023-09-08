import os
import pytest
import allure
# import urllib3
# urllib3.disable_warnings()

pytest.main(['-v','--alluredir', './result','--clean-alluredir'])

# pytest.main(['-v', '常州工业化运营平台_test.py','--alluredir', './result', '--clean-alluredir'])

os.system('allure generate ./result/ -o ./report_allure/ --clean')