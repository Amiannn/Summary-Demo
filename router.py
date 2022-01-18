from app import app

from controllers.summary import summary

from utils import router

# ============================================================================
# "                             BACKEND API                                  "
# ============================================================================

# Summary api
router.post(url='/summary/run' , controller=summary.run)