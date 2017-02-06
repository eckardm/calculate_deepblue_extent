from dappr.dappr import DAPPr
from dappr.config import dev, prod
import humanize

deepblue = DAPPr(
    prod.get("base_url"),
    prod.get("email"),
    prod.get("password")
)

collection_handle = raw_input("Collection Handle: ")
collection = deepblue.get_handle(collection_handle)

collection_size_bytes = 0

items = deepblue.get_collection_items(collection.get("id"))
for item in items:

    bitstreams = item.get("bitstreams")
    for bitstream in bitstreams:
        collection_size_bytes += bitstream.get("sizeBytes")

print humanize.naturalsize(collection_size_bytes)
