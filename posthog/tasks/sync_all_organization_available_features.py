from typing import cast
from collections.abc import Sequence

from posthog.models.organization import Organization


def sync_all_organization_available_features() -> None:
    for organization in cast(Sequence[Organization], Organization.objects.all().only("id")):
        organization.update_available_features()
        organization.save(update_fields=["available_features"])
