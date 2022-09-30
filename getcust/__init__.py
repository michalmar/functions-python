import logging
import azure.functions as func
import json

def main(req: func.HttpRequest, customerItem: func.DocumentList) -> str:
    if not customerItem:
        logging.warning("Customer item not found")
    else:
        logging.info("Found Customer item, id=%s",
                     customerItem[0]['id'])
        ret = {
                    "id": customerItem[0]['id'],
                    "firstname": customerItem[0]['firstname'],
                    "lastname": customerItem[0]['lastname'],
                    "email": customerItem[0]['email'],
                    "date": customerItem[0]['date1'],
                    "feat0": customerItem[0]['feat0'],
                    "feat1": customerItem[0]['feat1'],
                    "feat2": customerItem[0]['feat2'],
                    "feat3": customerItem[0]['feat3'],
               }
        return func.HttpResponse(
            json.dumps(ret),
            mimetype="application/json",

        )

    return 'OK'