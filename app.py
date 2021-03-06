#!/usr/bin/env python3

from aws_cdk import core

from session_tokens_app.pipeline_stack import PipelineStack


app = core.App()
PipelineStack(
    app,
    "web-pipe",
    env={
        "account": "871089662319",
        "region": "us-east-1",
    },
)

app.synth()
