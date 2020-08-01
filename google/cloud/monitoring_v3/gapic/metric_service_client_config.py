config = {
    "interfaces": {
        "google.monitoring.v3.MetricService": {
            "retry_codes": {
                "retry_policy_6_codes": ["DEADLINE_EXCEEDED", "UNAVAILABLE"],
                "no_retry_codes": [],
                "no_retry_3_codes": [],
            },
            "retry_params": {
                "no_retry_3_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 12000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 12000,
                    "total_timeout_millis": 12000,
                },
                "retry_policy_6_params": {
                    "initial_retry_delay_millis": 100,
                    "retry_delay_multiplier": 1.3,
                    "max_retry_delay_millis": 30000,
                    "initial_rpc_timeout_millis": 30000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 30000,
                    "total_timeout_millis": 30000,
                },
                "no_retry_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 0,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 0,
                    "total_timeout_millis": 0,
                },
            },
            "methods": {
                "ListMonitoredResourceDescriptors": {
                    "timeout_millis": 30000,
                    "retry_codes_name": "retry_policy_6_codes",
                    "retry_params_name": "retry_policy_6_params",
                },
                "GetMonitoredResourceDescriptor": {
                    "timeout_millis": 30000,
                    "retry_codes_name": "retry_policy_6_codes",
                    "retry_params_name": "retry_policy_6_params",
                },
                "ListMetricDescriptors": {
                    "timeout_millis": 30000,
                    "retry_codes_name": "retry_policy_6_codes",
                    "retry_params_name": "retry_policy_6_params",
                },
                "GetMetricDescriptor": {
                    "timeout_millis": 30000,
                    "retry_codes_name": "retry_policy_6_codes",
                    "retry_params_name": "retry_policy_6_params",
                },
                "CreateMetricDescriptor": {
                    "timeout_millis": 12000,
                    "retry_codes_name": "no_retry_3_codes",
                    "retry_params_name": "no_retry_3_params",
                },
                "DeleteMetricDescriptor": {
                    "timeout_millis": 30000,
                    "retry_codes_name": "retry_policy_6_codes",
                    "retry_params_name": "retry_policy_6_params",
                },
                "ListTimeSeries": {
                    "timeout_millis": 90000,
                    "retry_codes_name": "retry_policy_6_codes",
                    "retry_params_name": "retry_policy_6_params",
                },
                "CreateTimeSeries": {
                    "timeout_millis": 12000,
                    "retry_codes_name": "no_retry_3_codes",
                    "retry_params_name": "no_retry_3_params",
                },
            },
        }
    }
}
