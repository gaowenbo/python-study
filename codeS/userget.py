import json
import pandas as pd

data = pd.read_excel("d:\\python\\fk.xlsx")

data1 = data.values[1::3]
data1 = list(map(lambda x: str(x[1]).strip().replace(" ", "")[15: -25], data1))
print(data1)
data2 = data.values[0::3]
data2 = list(map(lambda x: str(x[1]).lstrip(), data2))
data21 = list(map(lambda x: str(x).split("//")[0][6:-2], data2))
data22 = list(map(lambda x: str(x).split("//")[1], data2))
print(data21)
print(data22)

strformat = '''
package com.zqsy.zys.openapi.service;

import com.zqsy.zys.openapi.strategy.HandlerMethodType;
import com.zqsy.zys.openapi.strategy.MethodStrategy;
import com.zqsy.zys.openapi.vo.OpenApiRequest;
import com.zqsy.zys.openapi.vo.OpenApiResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * @program: mankebao
 * @description: {}
 * @author: gaowenbo
 * @create: 2020-02-14 15:56
 */

@Service
@HandlerMethodType("{}")
public class {} implements MethodStrategy {{

    @Autowired
    private OpenApiService openApiService;

    @Override
    public OpenApiResponse handle(OpenApiRequest apiRequest) {{
        OpenApiResponse apiResponse = new OpenApiResponse();
        openApiService.{}(apiRequest, apiResponse);
        return apiResponse;
    }}
}}
'''

for i in range(len(data1)):
    file = open("D:\\mankebao\\mkb-main\\open_api\\src\\main\\java\\com\\zqsy\\zys\\openapi\\service\\" + data1[i] + "Service.java", "w", encoding="utf-8")
    file.write(strformat.format(data22[i], data21[i], data1[i] + "Service", data1[i]))
    file.close()