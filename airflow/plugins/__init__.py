from __future__ import division, absolute_import, print_function

from airflow.plugins_manager import AirflowPlugin

import operators
import helpers

# Defining the plugin class
class RoxPlugin(AirflowPlugin):
    name = "rox_plugin"
    operators = [
        operators.StageToRedshiftOperator,
        operators.DataQualityOperator
    ]
    helpers = [
    ]
