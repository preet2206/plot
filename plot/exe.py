# DO NOT TOUCH
# ============
# Auto generated code by 'nbox jobs new' command
# project name: plot
# created time: Monday W24 [ UTC 13 Jun, 2022 - 05:26:47 ]
#   created by: 
#
# > feeling stuck, start by populating the functions below <

import os
import sys
import fire


# the trick to importing nbox is to ensure proper loading order and setting
# of correct env vars, the first import is made in the user stub
os.environ["NBOX_JOB_FOLDER"] = os.getcwd() # Do not touch

from nbx_user import get_op, get_resource # << nbox imported here, fill all envs here

import nbox.utils as U
from nbox.nbxlib.tracer import Tracer
from nbox import Operator, nbox_grpc_stub
from nbox.hyperloop.nbox_ws_pb2 import UpdateRunRequest
from nbox.hyperloop.job_pb2 import Job
from nbox.messages import rpc
from nbox.messages import get_current_timestamp


def deploy():
  op: Operator = get_op()
  job = op.deploy(
    job_id_or_name = 'plot',
    workspace_id = '3oausmqp',
    resource = get_resource(), # use whatever the user has defined

    init_folder = U.folder(__file__), # ! ~ do not change this
  )


def run():
  op: Operator = get_op()
  op.propagate(_tracer = Tracer())
  if hasattr(op._tracer, "job_proto"):
    op.thaw(op._tracer.job_proto)

  try:
    op() # now we don't take anything as an input
  except Exception as e:
    U.logger.error(e)
    if hasattr(op._tracer, "job_proto"):
      op._tracer.job_proto.status = Job.Status.ERROR
  else:
    if hasattr(op._tracer, "job_proto"):
      op._tracer.job_proto.status = Job.Status.COMPLETED
      rpc(
        nbox_grpc_stub.UpdateRun, UpdateRunRequest(
          token = op._tracer.token, job=op._tracer.job_proto, updated_at=get_current_timestamp()
        ), "Failed to end job!"
      )

if __name__ == "__main__":
  fire.Fire({"deploy": deploy, "run": run})
  sys.exit(0)