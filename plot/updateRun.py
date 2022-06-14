#!/usr/bin/env python3
from nbox import nbox_grpc_stub

from nbox.messages import get_current_timestamp
from nbox.hyperloop.nbox_ws_pb2 import UpdateRunRequest
from nbox.hyperloop.job_pb2 import NBXAuthInfo, Job

def main(
  run_id: str = "jtmhawbk",
  job_id: str = "uk7x3dni",
  workspace_id: str = "3oausmqp"
):
  nbox_grpc_stub.UpdateRun(
    UpdateRunRequest(
      job = Job(
        id = job_id,
        auth_info = NBXAuthInfo(workspace_id = workspace_id),
        status = Job.Status.ERROR,
      ),
      token = run_id,
      updated_at = get_current_timestamp(),
    )
  )

if __name__ == "__main__":
  main()