# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl import LOG, async_network, connect
from dazl.protocols.events import ContractCreateEvent
from dazl.testing import SandboxLauncher
import pytest

from .dars import Simple


@pytest.mark.asyncio
async def test_static_dump_and_tail(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        party_info = await conn.allocate_party()

    async with async_network(url=sandbox.url, dars=Simple) as network:
        client = network.aio_party(party_info.party)
        seen_contracts = []

        @client.ledger_ready()
        def print_initial_state(event: ContractCreateEvent) -> None:
            LOG.info("Current ACS: %s", event.acs_find_active("*"))

        @client.ledger_created("*")
        def print_create(event: ContractCreateEvent) -> None:
            LOG.info("Seen cid: %s, cdata: %s", event.cid, event.cdata)
            seen_contracts.append(event.cid)

        network.start()

        await client.ready()

        for i in range(0, 5):
            await client.create(
                "Simple:OperatorNotification",
                {"operator": client.party, "theObservers": [], "text": "Something"},
            )

    assert len(seen_contracts) == 5
