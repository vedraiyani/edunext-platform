"""
Utility methods related to course
"""
import logging
from django.conf import settings

from opaque_keys.edx.keys import CourseKey
from microsite_configuration import microsite

log = logging.getLogger(__name__)


def get_lms_link_for_about_page(course_key):
    """
    Returns the url to the course about page.
    """
    assert isinstance(course_key, CourseKey)

    if settings.FEATURES.get('ENABLE_MKTG_SITE'):
        # Root will be "https://www.edx.org". The complete URL will still not be exactly correct,
        # but redirects exist from www.edx.org to get to the Drupal course about page URL.
        about_base = settings.MKTG_URLS['ROOT']
    else:
        about_base = settings.LMS_ROOT_URL

    # eduNEXT 23.12.2015 make the link microsite aware, based on the org of the course
    about_base = microsite.get_value_for_org(course_key.org, 'SITE_NAME', about_base)

    return u"{about_base_url}/courses/{course_key}/about".format(
        about_base_url=about_base,
        course_key=course_key.to_deprecated_string()
    )
