import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
