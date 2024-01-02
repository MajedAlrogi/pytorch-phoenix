# tests in this list will run without Dynamo strict mode by default.
FIXME_default_non_strict = {
    "backends/xeon/test_launch",
    "benchmark_utils/test_benchmark_utils",
    "distributions/test_constraints",
    "distributions/test_distributions",
    "dynamo/test_activation_checkpointing",
    "dynamo/test_after_aot",
    "dynamo/test_aot_autograd",
    "dynamo/test_autograd_function",
    "dynamo/test_backends",
    "dynamo/test_backward_higher_order_ops",
    "dynamo/test_base_output",
    "dynamo/test_bytecode_hook",
    "dynamo/test_compile",
    "dynamo/test_comptime",
    "dynamo/test_config",
    "dynamo/test_ctx_manager",
    "dynamo/test_cudagraphs",
    "dynamo/test_debug_utils",
    "dynamo/test_decorators",
    "dynamo/test_dynamic_shapes",
    "dynamo/test_exc",
    "dynamo/test_export",
    "dynamo/test_export_mutations",
    "dynamo/test_frame_init",
    "dynamo/test_functions",
    "dynamo/test_global",
    "dynamo/test_higher_order_ops",
    "dynamo/test_hooks",
    "dynamo/test_input_attr_tracking",
    "dynamo/test_interop",
    "dynamo/test_logging",
    "dynamo/test_minifier",
    "dynamo/test_misc",
    "dynamo/test_model_output",
    "dynamo/test_modules",
    "dynamo/test_nops",
    "dynamo/test_optimizers",
    "dynamo/test_pre_dispatch",
    "dynamo/test_profiler",
    "dynamo/test_python_autograd",
    "dynamo/test_recompile_ux",
    "dynamo/test_recompiles",
    "dynamo/test_replay_record",
    "dynamo/test_repros",
    "dynamo/test_skip_non_tensor",
    "dynamo/test_sources",
    "dynamo/test_subclasses",
    "dynamo/test_subgraphs",
    "dynamo/test_torchrec",
    "dynamo/test_trace_rules",
    "dynamo/test_unspec",
    "dynamo/test_verify_correctness",
    "export/test_db",
    "export/test_export",
    "export/test_export_nonstrict",
    "export/test_functionalized_assertions",
    "export/test_pass_infra",
    "export/test_passes",
    "export/test_retraceability",
    "export/test_serdes",
    "export/test_serialize",
    "export/test_unflatten",
    "export/test_upgrade",
    "export/test_verifier",
    "functorch/test_aotdispatch",
    "functorch/test_control_flow",
    "functorch/test_dims",
    "functorch/test_eager_transforms",
    "functorch/test_logging",
    "functorch/test_memory_efficient_fusion",
    "functorch/test_minifier",
    "functorch/test_ops",
    "functorch/test_parsing",
    "functorch/test_rearrange",
    "functorch/test_vmap",
    "functorch/test_vmap_registrations",
    "inductor/test_aot_inductor",
    "inductor/test_aot_inductor_utils",
    "inductor/test_benchmark_fusion",
    "inductor/test_binary_folding",
    "inductor/test_codecache",
    "inductor/test_codegen_triton",
    "inductor/test_compiled_autograd",
    "inductor/test_compiled_optimizers",
    "inductor/test_config",
    "inductor/test_coordinate_descent_tuner",
    "inductor/test_cpu_cpp_wrapper",
    "inductor/test_cpu_repro",
    "inductor/test_cuda_cpp_wrapper",
    "inductor/test_cuda_repro",
    "inductor/test_cudacodecache",
    "inductor/test_cudagraph_trees",
    "inductor/test_custom_lowering",
    "inductor/test_custom_post_grad_passes",
    "inductor/test_debug_trace",
    "inductor/test_dependencies",
    "inductor/test_efficient_conv_bn_eval",
    "inductor/test_extension_backend",
    "inductor/test_foreach",
    "inductor/test_fp8",
    "inductor/test_fused_attention",
    "inductor/test_fx_fusion",
    "inductor/test_group_batch_fusion",
    "inductor/test_indexing",
    "inductor/test_inductor_freezing",
    "inductor/test_inductor_utils",
    "inductor/test_inplacing_pass",
    "inductor/test_kernel_benchmark",
    "inductor/test_layout_optim",
    "inductor/test_max_autotune",
    "inductor/test_memory_planning",
    "inductor/test_minifier",
    "inductor/test_minifier_isolate",
    "inductor/test_mkldnn_pattern_matcher",
    "inductor/test_mmdecomp",
    "inductor/test_move_constructors_to_cuda",
    "inductor/test_pattern_matcher",
    "inductor/test_perf",
    "inductor/test_profiler",
    "inductor/test_select_algorithm",
    "inductor/test_smoke",
    "inductor/test_snode_runtime",
    "inductor/test_split_cat_fx_passes",
    "inductor/test_standalone_compile",
    "inductor/test_torchinductor",
    "inductor/test_torchinductor_codegen_dynamic_shapes",
    "inductor/test_torchinductor_dynamic_shapes",
    "inductor/test_torchinductor_opinfo",
    "inductor/test_triton_heuristics",
    "inductor/test_triton_wrapper",
    "inductor/test_unbacked_symints",
    "lazy/test_bindings",
    "lazy/test_debug_util",
    "lazy/test_extract_compiled_graph",
    "lazy/test_functionalization",
    "lazy/test_generator",
    "lazy/test_meta_kernel",
    "lazy/test_reuse_ir",
    "lazy/test_step_closures",
    "lazy/test_ts_opinfo",
    "nn/test_convolution",
    "nn/test_dropout",
    "nn/test_embedding",
    "nn/test_init",
    "nn/test_lazy_modules",
    "nn/test_module_hooks",
    "nn/test_multihead_attention",
    "nn/test_packed_sequence",
    "nn/test_parametrization",
    "nn/test_pooling",
    "nn/test_pruning",
    "optim/test_lrscheduler",
    "optim/test_optim",
    "optim/test_swa_utils",
    "profiler/test_memory_profiler",
    "profiler/test_profiler",
    "profiler/test_profiler_tree",
    "test_ao_sparsity",
    "test_autograd",
    "test_binary_ufuncs",
    "test_bundled_inputs",
    "test_comparison_utils",
    "test_compile_benchmark_util",
    "test_complex",
    "test_content_store",
    "test_cpp_api_parity",
    "test_cpp_extensions_aot_ninja",
    "test_cpp_extensions_aot_no_ninja",
    "test_cpp_extensions_jit",
    "test_cpp_extensions_open_device_registration",
    "test_cuda",
    "test_cuda_expandable_segments",
    "test_cuda_multigpu",
    "test_cuda_nvml_based_avail",
    "test_cuda_primary_ctx",
    "test_cuda_sanitizer",
    "test_cuda_trace",
    "test_dataloader",
    "test_datapipe",
    "test_decomp",
    "test_deploy",
    "test_dispatch",
    "test_dlpack",
    "test_dynamic_shapes",
    "test_expanded_weights",
    "test_fake_tensor",
    "test_flop_counter",
    "test_foreach",
    "test_function_schema",
    "test_functional_autograd_benchmark",
    "test_functionalization",
    "test_functionalization_of_rng_ops",
    "test_futures",
    "test_fx",
    "test_fx_experimental",
    "test_fx_passes",
    "test_fx_reinplace_pass",
    "test_hub",
    "test_import_stats",
    "test_itt",
    "test_jit",
    "test_jit_autocast",
    "test_jit_disabled",
    "test_jit_fuser_te",
    "test_jit_llga_fuser",
    "test_jiterator",
    "test_legacy_vmap",
    "test_license",
    "test_linalg",
    "test_logging",
    "test_masked",
    "test_maskedtensor",
    "test_matmul_cuda",
    "test_meta",
    "test_mkl_verbose",
    "test_mkldnn",
    "test_mkldnn_fusion",
    "test_mkldnn_verbose",
    "test_mobile_optimizer",
    "test_model_dump",
    "test_model_exports_to_core_aten",
    "test_module_init",
    "test_modules",
    "test_monitor",
    "test_multiprocessing",
    "test_multiprocessing_spawn",
    "test_namedtensor",
    "test_namedtuple_return_api",
    "test_native_functions",
    "test_native_mha",
    "test_nestedtensor",
    "test_nn",
    "test_numba_integration",
    "test_numpy_interop",
    "test_openmp",
    "test_ops",
    "test_ops_fwd_gradients",
    "test_ops_gradients",
    "test_ops_jit",
    "test_optim",
    "test_out_dtype_op",
    "test_overrides",
    "test_package",
    "test_per_overload_api",
    "test_prims",
    "test_proxy_tensor",
    "test_pruning_op",
    "test_public_bindings",
    "test_python_dispatch",
    "test_pytree",
    "test_quantization",
    "test_reductions",
    "test_scatter_gather_ops",
    "test_schema_check",
    "test_segment_reductions",
    "test_serialization",
    "test_set_default_mobile_cpu_allocator",
    "test_shape_ops",
    "test_show_pickle",
    "test_sort_and_select",
    "test_sparse",
    "test_sparse_csr",
    "test_sparse_semi_structured",
    "test_spectral_ops",
    "test_stateless",
    "test_subclass",
    "test_sympy_utils",
    "test_tensor_creation_ops",
    "test_tensorboard",
    "test_tensorexpr",
    "test_tensorexpr_pybind",
    "test_testing",
    "test_transformers",
    "test_type_hints",
    "test_type_info",
    "test_type_promotion",
    "test_typing",
    "test_unary_ufuncs",
    "test_utils",
    "test_view_ops",
    "test_vulkan",
    "test_weak",
    "test_xnnpack_integration",
    "torch_np/numpy_tests/core/test_dlpack",
    "torch_np/numpy_tests/core/test_dtype",
    "torch_np/numpy_tests/core/test_einsum",
    "torch_np/numpy_tests/core/test_getlimits",
    "torch_np/numpy_tests/core/test_indexing",
    "torch_np/numpy_tests/core/test_multiarray",
    "torch_np/numpy_tests/core/test_numeric",
    "torch_np/numpy_tests/core/test_numerictypes",
    "torch_np/numpy_tests/core/test_scalar_ctors",
    "torch_np/numpy_tests/core/test_scalar_methods",
    "torch_np/numpy_tests/core/test_scalarinherit",
    "torch_np/numpy_tests/core/test_scalarmath",
    "torch_np/numpy_tests/core/test_shape_base",
    "torch_np/numpy_tests/fft/test_helper",
    "torch_np/numpy_tests/fft/test_pocketfft",
    "torch_np/numpy_tests/lib/test_arraypad",
    "torch_np/numpy_tests/lib/test_arraysetops",
    "torch_np/numpy_tests/lib/test_function_base",
    "torch_np/numpy_tests/lib/test_histograms",
    "torch_np/numpy_tests/lib/test_index_tricks",
    "torch_np/numpy_tests/lib/test_shape_base_",
    "torch_np/numpy_tests/lib/test_twodim_base",
    "torch_np/numpy_tests/lib/test_type_check",
    "torch_np/numpy_tests/linalg/test_linalg",
    "torch_np/test_basic",
    "torch_np/test_binary_ufuncs",
    "torch_np/test_dtype",
    "torch_np/test_function_base",
    "torch_np/test_ndarray_methods",
    "torch_np/test_nep50_examples",
    "torch_np/test_random",
    "torch_np/test_reductions",
    "torch_np/test_scalars_0D_arrays",
    "torch_np/test_ufuncs_basic",
    "torch_np/test_unary_ufuncs",
}

# We generate unittest.expectedFailure for all of the following tests
# when run under PYTORCH_TEST_WITH_DYNAMO=1.
#
# This lists exists so we can more easily add large numbers of failing tests,
dynamo_expected_failures = {
    "TestCppExtensionJIT.test_cpp_frontend_module_has_up_to_date_attribute",
    "TestCppExtensionJIT.test_custom_compound_op_autograd",
    "TestCppExtensionJIT.test_cpp_frontend_module_has_up_to_date_attributes",
    "TestCppExtensionOpenRgistration.test_open_device_registration",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_ge_cpu",
    "TestTorchDeviceTypeCPU.test_normal_kstest_cpu_float64",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_pow_cpu",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_lerp_cpu",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_fmod_cpu",
    "TestTorch.test_tensoriterator_output_setup",
    "TestTorch.test_pin_memory",
    "TestTorchDeviceTypeCPU.test_exponential_kstest_cpu_float64",
    "TestTorchDeviceTypeCPU.test_normal_kstest_cpu_float32",
    "TestTorchDeviceTypeCPU.test_nondeterministic_alert_MaxUnpool3d_cpu_float64",
    "TestTorch.test_newaxis_numpy_comparison",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_masked_scatter_cpu",
    "TestTorchDeviceTypeCPU.test_untyped_storage_meta_cpu",
    "TestTorch.test_upsample_nearest1d_meta",
    "TestTorchDeviceTypeCPU.test_memory_format_operators_cpu",
    "TestTorch.test_contains",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_masked_fill_cpu",
    "TestTorchDeviceTypeCPU.test_nondeterministic_alert_MaxUnpool2d_cpu_float64",
    "TestTorch.test_parsing_int64",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_dist_cpu",
    "TestTorchDeviceTypeCPU.test_nondeterministic_alert_MaxUnpool1d_cpu_float64",
    "TestTorchDeviceTypeCPU.test_nondeterministic_resize_quantized_cpu_quint4x2",
    "TestTorch.test_map",
    "TestTorchDeviceTypeCPU.test_normal_kstest_cpu_float16",
    "TestTorchDeviceTypeCPU.test_nondeterministic_alert_MaxUnpool1d_cpu_float32",
    "TestTorch.test_parsing_double",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_lt_cpu",
    "TestTorch.test_upsample_nearest2d_meta",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_addcdiv_cpu",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_remainder_cpu",
    "TestTorchDeviceTypeCPU.test_nondeterministic_resize_quantized_cpu_quint2x4",
    "TestTorchDeviceTypeCPU.test_uniform_kstest_cpu_float64",
    "TestTorch.test_cuda_not_built",
    "TestTorchDeviceTypeCPU.test_exponential_kstest_cpu_bfloat16",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_min_cpu",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_masked_select_cpu",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_le_cpu",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_copy_cpu",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_max_cpu",
    "TestTorch.test_bmm_multithreaded",
    "TestTorchDeviceTypeCPU.test_nondeterministic_alert_MaxUnpool3d_cpu_float32",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_atan2_cpu",
    "TestTorchDeviceTypeCPU.test_where_scalar_handcrafted_values_cpu",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_div_cpu",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_map2_cpu",
    "TestTorch.test_type",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_eq_cpu",
    "TestTorch.test_new",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_ne_cpu",
    "TestTorchDeviceTypeCPU.test_nondeterministic_resize_quantized_cpu_quint8",
    "TestTorchDeviceTypeCPU.test_uniform_kstest_cpu_bfloat16",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_gt_cpu",
    "TestTorchDeviceTypeCPU.test_exponential_kstest_cpu_float32",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_add_cpu",
    "TestTorchDeviceTypeCPU.test_nondeterministic_alert_MaxUnpool2d_cpu_float32",
    "TestTorch.test_parsing_intlist",
    "TestTorchDeviceTypeCPU.test_nondeterministic_resize_quantized_cpu_qint32",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_addcmul_cpu",
    "TestTorchDeviceTypeCPU.test_nondeterministic_resize_quantized_cpu_qint8",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_map_cpu",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_mul_cpu",
    "TestTorchDeviceTypeCPU.test_uniform_kstest_cpu_float32",
    "TestTorchDeviceTypeCPU.test_exponential_kstest_cpu_float16",
    "TestTorchDeviceTypeCPU.test_uniform_kstest_cpu_float16",
    "TestTorchDeviceTypeCPU.test_broadcast_fn_sub_cpu",
    "TestTorch.test_storage_casts",
    "TestTorch.test_terminate_handler_on_crash",
    "TestAutogradFallback.test_supports_tensor_lists_mode_nothing",
    "TestAutogradFallback.test_post_autograd_returns_mix_of_requires_grad_tensors_mode_warn",
    "TestAutogradFallback.test_cpu_return_self_mode_warn",
    "TestAutogradFallback.test_base_does_not_require_grad_mode_warn",
    "TestAutogradFallback.test_undefined_grads_mode_nothing",
    "TestAutogradFallback.test_undefined_grads_mode_warn",
    "TestAutogradFallback.test_autograd_function_registered_to_cpu_mode_warn",
    "TestAutogradFallback.test_cpu_return_self_mode_nothing",
    "TestAutogradFallback.test_composite_registered_to_cpu_mode_nothing",
    "TestAutogradFallback.test_undefined_inputs_outputs_mode_nothing",
    "TestAutogradFallback.test_no_autograd_kernel_inplace_mode_nothing",
    "TestAutogradFallback.test_post_autograd_returns_leaf_mode_nothing",
    "TestAutogradFallback.test_inplace_on_tensor_that_does_not_require_grad_mode_nothing",
    "TestAutogradFallback.test_no_grad_mode_warn",
    "TestAutogradFallback.test_inplace_autograd_function_registered_to_cpu_mode_warn",
    "TestAutogradFallback.test_no_autograd_kernel_mode_warn",
    "TestAutogradFallback.test_base_does_not_require_grad_mode_nothing",
    "TestAutogradFallback.test_composite_registered_to_cpu_mode_warn",
    "TestAutogradFallback.test_post_autograd_returns_mix_of_requires_grad_tensors_mode_nothing",
    "TestAutogradFallback.test_no_autograd_kernel_inplace_mode_warn",
    "TestAutogradFallback.test_no_grad_mode_nothing",
    "TestAutogradFallback.test_no_autograd_kernel_mode_nothing",
    "TestAutogradFallback.test_supports_tensor_lists_mode_warn",
    "TestAutogradFallback.test_post_autograd_returns_leaf_mode_warn",
    "TestAutogradFallback.test_undefined_inputs_outputs_mode_warn",
    "TestAutogradFallback.test_inplace_on_tensor_that_does_not_require_grad_mode_warn",
    "TestAutogradFallback.test_inplace_autograd_function_registered_to_cpu_mode_nothing",
    "TestAutogradFallback.test_autograd_function_registered_to_cpu_mode_nothing",
    "MiniOpTest.test_no_abstract",
    "TestCustomOp.test_lifetime",
    "TestCustomOp.test_backward_dict_grad_for_nontensor",
    "TestCustomOp.test_backward_impl_on_existing_op",
    "TestCustomOp.test_define_with_tags_list",
    "TestCustomOp.test_impl_meta",
    "TestCustomOp.test_new_data_dependent_symint",
    "MiniOpTest.test_aot_dispatch_static__test_no_abstract",
    "TestCustomOp.test_impl_cpu",
    "TestCustomOp.test_define_with_tags_single",
    "TestCustomOp.test_backward_partially_registered",
    "TestCustomOp.test_backward_output_differentiability_non_tensor",
    "TestCustomOp.test_supported_return_types_single_return",
    "TestCustomOp.test_duplicate_impl",
    "TestCustomOp.test_define_with_tags_tuple",
    "TestCustomOp.test_impl_on_existing_op",
    "TestCustomOp.test_backward_dict_requires_keys_for_input_tensors",
    "TestCustomOp.test_backward_returns_dict",
    "TestCustomOp.test_backward_dict_requires_keys_for_input_optional_tensors",
    "TestCustomOp.test_builtin_torchscript_ops",
    "TestCustomOp.test_save_for_backward_inputs_are_namedtuple",
    "TestCustomOpTestingCPU.test_autograd_registered_at_backend_cpu",
    "TestCustomOpTestingCPU.test_incorrect_schema_view_cpu",
    "TestCustomOp.test_define_and_impl",
    "TestCustomOp.test_impl_device_function",
    "TestCustomOp.test_supported_return_types_multi_return",
    "TestCustomOpTestingCPU.test_missing_abstract_impl_cpu",
    "TestCustomOp.test_builtin_aten_ops_are_pt2_compliant",
    "TestCustomOp.test_autograd_notimplemented_gradmode",
    "MiniOpTest.test_faketensor__test_no_abstract",
    "TestCustomOpTestingCPU.test_incorrect_schema_mutation_cpu",
    "TestGenerateOpcheckTests.test_opcheck_bad_op",
    "TestCustomOp.test_backward_output_differentiability_tensorlist",
    "TestCustomOp.test_legacy_impl",
    "TestCustomOpTestingCPU.test_incorrect_abstract_impl_cpu",
    "MiniOpTest.test_schema__test_no_abstract",
    "TestCustomOpTestingCPU.test_autograd_registration_check_incorrect_composite_cpu",
    "TestCustomOp.test_basic_make_fx",
    "TestCustomOp.test_backward_output_differentiability_numel",
    "TestCustomOp.test_backward_tensorlist_input_requires_list_grads",
    "TestCustomOp.test_not_implemented_error",
    "TestCustomOp.test_autogen_aten_ops_are_pt2_compliant",
    "TestCustomOp.test_supported_param_types",
    "TestCustomOp.test_impl_function",
    "TestCustomOp.test_impl_invalid_devices",
    "MiniOpTest.test_autograd_registration__test_no_abstract",
    "TestCustomOp.test_backward_tensorlist_input_requires_list_grads_none_or_Tensor",
    "TestCustomOp.test_legacy_define",
    "TestCustomOpTestingCPU.test_missing_functionalization_cpu",
    "TestCustomOp.test_backward_grads_are_tensor_or_none",
    "TestCustomOp.test_impl_device_cpu",
    "MiniOpTest.test_aot_dispatch_dynamic__test_no_abstract",
    "TestCustomOpTestingCPU.test_autograd_registration_check_incorrect_cpu",
    "TestCustomOpTestingCPU.test_opcheck_fails_basic_cpu",
    "TestCustomOp.test_autograd_notimplemented",
    "TestCustomOp.test_backward_output_differentiability_type",
    "TestCustomOp.test_backward_dict_invalid_keys",
    "TestCustomOp.test_backward_tensorlist_input_requires_list_grads_with_same_numel",
    "TestCustomOp.test_sequences",
    "TestCustomOp.test_impl_on_existing_op_with_cpu_registration_key_CUDA",
    "TestCustomOp.test_impl_on_existing_op_with_cpu_registration_key_CPU",
    "TestCustomOp.test_impl_on_existing_op_with_cpu_registration_key_CompositeExplicitAutograd",
    "TestCustomOp.test_supported_schemas",
    "TestFunctionalOptimParity.test_functional_optim_parity_sgd",
    "TestIndexingCPU.test_invalid_index_cpu",
    "NumpyTestsCPU.test_boolean_shape_mismatch_cpu",
    "TestIndexingCPU.test_empty_ndim_index_bool_cpu",
    "TestIndexingCPU.test_out_of_bound_index_cpu",
    "NumpyTestsCPU.test_index_no_floats_cpu",
    "TestIndexingCPU.test_zero_dim_index_cpu",
    "NumpyTestsCPU.test_empty_fancy_index_cpu",
    "TestIndexingCPU.test_index_cpu",
    "TestIndexingCPU.test_index_limits_cpu",
    "NumpyTestsCPU.test_boolean_indexing_weirdness_cpu",
}

dynamo_skips = {}
