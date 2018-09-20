
def main():
    callstack_raw = """
    	[0xC9962D48] Java_aa_bb_cc_JNICallStudy_stringFromJNI(JNIEnv * env, jobject thiz) Line 15	C++
     	[0xE3B1AA7A] libart.so!art_quick_generic_jni_trampoline()	C++
     	[0xE3B16576] libart.so!art_quick_invoke_stub_internal()	C++
     	[0xE3AEFB7C] libart.so!art_quick_invoke_stub()	C++
     	[0xE37AA018] libart.so!art::ArtMethod::Invoke(art::Thread*, unsigned int*, unsigned int, art::JValue*, char const*)()	C++
     	[0xE38EEAEC] libart.so!art::interpreter::ArtInterpreterToCompiledCodeBridge(art::Thread*, art::ArtMethod*, art::ShadowFrame*, unsigned short, art::JValue*)()	C++
     	[0xE38E95DA] libart.so!bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()	C++
     	[0xE39102DE] libart.so!bool art::interpreter::DoInvoke<(art::InvokeType)2, false, false>(art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()	C++
     	[0xE390E8A4] libart.so!void art::interpreter::ExecuteSwitchImplCpp<false, false>(art::interpreter::SwitchImplContext*)()	C++
     	[0xE3B1B456] libart.so!ExecuteSwitchImplAsm()	C++
     	[0xE38CDD1A] libart.so!art::interpreter::Execute(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame&, art::JValue, bool) [clone .llvm.2471763592]()	C++
     	[0xE38D243C] libart.so!art::interpreter::ArtInterpreterToInterpreterBridge(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*, art::JValue*)()	C++
     	[0xE38E95C2] libart.so!bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()	C++
     	[0xE3911BAE] libart.so!bool art::interpreter::DoInvoke<(art::InvokeType)4, false, false>(art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()	C++
     	[0xE390C3DC] libart.so!void art::interpreter::ExecuteSwitchImplCpp<false, false>(art::interpreter::SwitchImplContext*)()	C++
     	[0xE3B1B456] libart.so!ExecuteSwitchImplAsm()	C++
     	[0xE38CDD1A] libart.so!art::interpreter::Execute(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame&, art::JValue, bool) [clone .llvm.2471763592]()	C++
     	[0xE38D243C] libart.so!art::interpreter::ArtInterpreterToInterpreterBridge(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*, art::JValue*)()	C++
     	[0xE38E95C2] libart.so!bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()	C++
     	[0xE3912400] libart.so!bool art::interpreter::DoInvoke<(art::InvokeType)0, false, false>(art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()	C++
     	[0xE390F440] libart.so!void art::interpreter::ExecuteSwitchImplCpp<false, false>(art::interpreter::SwitchImplContext*)()	C++
     	[0xE3B1B456] libart.so!ExecuteSwitchImplAsm()	C++
     	[0xE38CDD1A] libart.so!art::interpreter::Execute(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame&, art::JValue, bool) [clone .llvm.2471763592]()	C++
     	[0xE38D243C] libart.so!art::interpreter::ArtInterpreterToInterpreterBridge(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*, art::JValue*)()	C++
     	[0xE38E95C2] libart.so!bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()	C++
     	[0xE39102DE] libart.so!bool art::interpreter::DoInvoke<(art::InvokeType)2, false, false>(art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()	C++
     	[0xE390E8A4] libart.so!void art::interpreter::ExecuteSwitchImplCpp<false, false>(art::interpreter::SwitchImplContext*)()	C++
     	[0xE3B1B456] libart.so!ExecuteSwitchImplAsm()	C++
     	[0xE38CDD1A] libart.so!art::interpreter::Execute(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame&, art::JValue, bool) [clone .llvm.2471763592]()	C++
     	[0xE38D243C] libart.so!art::interpreter::ArtInterpreterToInterpreterBridge(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*, art::JValue*)()	C++
     	[0xE38E95C2] libart.so!bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()	C++
     	[0xE3AEB7B2] libart.so!MterpInvokeStatic()	C++
     	[0xE3B09498] libart.so!ExecuteMterpImpl()	C++
     	[0xE38CDD56] libart.so!art::interpreter::Execute(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame&, art::JValue, bool) [clone .llvm.2471763592]()	C++
     	[0xE38D2382] libart.so!art::interpreter::EnterInterpreterFromEntryPoint(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*)()	C++
     	[0xE3ADE2BC] libart.so!artQuickToInterpreterBridge()	C++
     	[0xE3B1AB02] libart.so!art_quick_to_interpreter_bridge()	C++
     	[0xE3B1ABF0] libart.so!art_quick_instrumentation_entry()	C++
     	[0xE3902CB0] libart.so!??()	C++
     	app_process32!??()	C++
    """
    
    callstack_list = callstack_raw.split()[0:-2]

    for line in callstack_list:
		print(line)

    print(callstack_list)


def cal_address():
    addr_list = [ 
    	(0xC9962D48,"Java_aa_bb_cc_JNICallStudy_stringFromJNI(JNIEnv * env, jobject thiz) Line 15"),
     	(0xE3B1AA7A,"libart.so!art_quick_generic_jni_trampoline()"),
     	(0xE3B16576,"libart.so!art_quick_invoke_stub_internal()"),
     	(0xE3AEFB7C,"libart.so!art_quick_invoke_stub()"),
     	(0xE37AA018,"libart.so!art::ArtMethod::Invoke(art::Thread*, unsigned int*, unsigned int, art::JValue*, char const*)()"),
     	(0xE38EEAEC,"libart.so!art::interpreter::ArtInterpreterToCompiledCodeBridge(art::Thread*, art::ArtMethod*, art::ShadowFrame*, unsigned short, art::JValue*)()"),
     	(0xE38E95DA,"libart.so!bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()"),
     	(0xE39102DE,"libart.so!bool art::interpreter::DoInvoke<(art::InvokeType)2, false, false>(art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()"),
     	(0xE390E8A4,"libart.so!void art::interpreter::ExecuteSwitchImplCpp<false, false>(art::interpreter::SwitchImplContext*)()"),
     	(0xE3B1B456,"libart.so!ExecuteSwitchImplAsm()"),
     	(0xE38CDD1A,"libart.so!art::interpreter::Execute(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame&, art::JValue, bool) [clone .llvm.2471763592]()"),
     	(0xE38D243C,"libart.so!art::interpreter::ArtInterpreterToInterpreterBridge(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*, art::JValue*)()"),
     	(0xE38E95C2,"libart.so!bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()"),
     	(0xE3911BAE,"libart.so!bool art::interpreter::DoInvoke<(art::InvokeType)4, false, false>(art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()"),
     	(0xE390C3DC,"libart.so!void art::interpreter::ExecuteSwitchImplCpp<false, false>(art::interpreter::SwitchImplContext*)()"),
     	(0xE3B1B456,"libart.so!ExecuteSwitchImplAsm()"),
     	(0xE38CDD1A,"libart.so!art::interpreter::Execute(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame&, art::JValue, bool) [clone .llvm.2471763592]()"),
     	(0xE38D243C,"libart.so!art::interpreter::ArtInterpreterToInterpreterBridge(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*, art::JValue*)()"),
     	(0xE38E95C2,"libart.so!bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()"),
     	(0xE3912400,"libart.so!bool art::interpreter::DoInvoke<(art::InvokeType)0, false, false>(art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()"),
     	(0xE390F440,"libart.so!void art::interpreter::ExecuteSwitchImplCpp<false, false>(art::interpreter::SwitchImplContext*)()"),
     	(0xE3B1B456,"libart.so!ExecuteSwitchImplAsm()"),
     	(0xE38CDD1A,"libart.so!art::interpreter::Execute(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame&, art::JValue, bool) [clone .llvm.2471763592]()"),
     	(0xE38D243C,"libart.so!art::interpreter::ArtInterpreterToInterpreterBridge(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*, art::JValue*)()"),
     	(0xE38E95C2,"libart.so!bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()"),
     	(0xE39102DE,"libart.so!bool art::interpreter::DoInvoke<(art::InvokeType)2, false, false>(art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()"),
     	(0xE390E8A4,"libart.so!void art::interpreter::ExecuteSwitchImplCpp<false, false>(art::interpreter::SwitchImplContext*)()"),
     	(0xE3B1B456,"libart.so!ExecuteSwitchImplAsm()"),
     	(0xE38CDD1A,"libart.so!art::interpreter::Execute(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame&, art::JValue, bool) [clone .llvm.2471763592]()"),
     	(0xE38D243C,"libart.so!art::interpreter::ArtInterpreterToInterpreterBridge(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*, art::JValue*)()"),
     	(0xE38E95C2,"libart.so!bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)()"),
     	(0xE3AEB7B2,"libart.so!MterpInvokeStatic()"),
     	(0xE3B09498,"libart.so!ExecuteMterpImpl()"),
     	(0xE38CDD56,"libart.so!art::interpreter::Execute(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame&, art::JValue, bool) [clone .llvm.2471763592]()"),
     	(0xE38D2382,"libart.so!art::interpreter::EnterInterpreterFromEntryPoint(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*)()"),
     	(0xE3ADE2BC,"libart.so!artQuickToInterpreterBridge()"),
     	(0xE3B1AB02,"libart.so!art_quick_to_interpreter_bridge()"),
     	(0xE3B1ABF0,"libart.so!art_quick_instrumentation_entry()"),
     	(0xE3902CB0,"libart.so!??()"),
    ]  
    
    for (addr,caller) in addr_list:
        print("{}:{:>7.4f}G :{}".format(hex(addr).upper(),addr/1024/1024/1024.0,caller))

if __name__ == "__main__":
   # main()
   cal_address()
