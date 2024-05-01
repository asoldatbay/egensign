import requests


class ConvertAPIService:

    @staticmethod
    def docx_to_pdf(file64):
        r = requests.post(
            url="https://v2.convertapi.com/convert/docx/to/pdf?Secret=AE3llQNCOvHaDcNh",
            json={
                "Parameters": [
                    {
                        "Name": "File",
                        "FileValue": {
                            "Name": f"my_file.docx",
                            "Data": file64.decode('utf-8')
                        }
                    }
                ]
            }
        )
        r.raise_for_status()

        return r.json(), "application/pdf"
