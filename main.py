import random,os
sys_val_key = "80218021"
code1 = input("Enter system validation Key:\n")
if code1 == sys_val_key: 
    os.system('clear')
    pass
else:
    for i in range(50): print(random.randint(1111111111, 9999999999))
    os._exit(0)
import sys,json,re,platform,math,urllib.parse,urllib.request,importlib,py_compile,threading,time
M_PATH,MEM_PATH="./model.gguf","./memory.json"
models = """
Choose your Model:
     - 1: Gemma4
     - 2: Claude Sonnet
     - 3: Qwen:1.5B:2.4Q
     - 4: Raphael's AI
     - 5: Gemini
     - 6: Copilot
     - 7: Code_Sandbox"""
gemma4 = "Your model is Gemm4. You specialize in advanced reasoning and on-device intelligence."
claude_s = "Your model is Claude Sonnet. You specialize in enterprise knowledge, coding, and tool use."
qwen = "Your model is Qwen. You specialize in vocabulary and language."
ai_r = "Your model is a custom-made powerful model. You specialize in... well... everything."
gemini = "Your model is gemini. You specialize in token-effecient responses, and massive context understanding."
Copilot = "Your model is Copilot. You specialize in advanced reasoning, and context aware enterprise flows."
cs = "Your model is a custom-made model focused on coding. You are versatile in every single possible coding language."
try:
    import llama_cpp;from llama_cpp import Llama;REAL_AI=True
except ImportError:REAL_AI=False
try:
    import nltk;nltk.data.path.append(os.path.abspath("./dictionary"))
except ImportError:pass
def tool_web_scrape(u):
    try:
        clean_q=urllib.parse.quote_plus(str(u).strip())
        t=f"https://duckduckgo.com{clean_q}"
        req=urllib.request.Request(t,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req,timeout=8) as s:r=s.read().decode('utf-8',errors='ignore')
        text=re.sub(r'\s+',' ',re.sub(r'<script.*?</script>|<style.*?</style>|<[^>]+>',' ',r,flags=re.DOTALL)).strip()
        return text[:1500] if text else "No search results returned."
    except Exception as e:return f"Scraper network fallback error: {e}"
def tool_execute_code(c):
    try:
        v={};from io import StringIO;old=sys.stdout;out=StringIO();sys.stdout=out;l=c.replace(';','\n').strip().split('\n')
        if l and not l[-1].strip().startswith('print') and 'print(' not in l[-1] and '=' not in l[-1] and not l[-1].strip().startswith('def '):l[-1]=f"__res__ = {l[-1]}"
        exec("\n".join(l),{},v);sys.stdout=old;cap=out.getvalue();ret="--- CORESANDBOX OUTPUT ---\n"
        if cap:ret+=f"Console Logs:\n{cap.strip()}\n"
        if '__res__' in v:ret+=f"Calculated Result: {v['__res__']}\n"
        elif v:ret+=f"Tracked States: { {k:v[k] for k in v if not k.startswith('_')} }\n"
        return ret+"-------------------------"
    except Exception as e:
        if 'old' in locals():sys.stdout=old
        return f"Code runtime error: {e}"
def tool_generate_plugin(n,c):
    p_dir="./plugins";os.makedirs(p_dir,exist_ok=True);p_file=os.path.join(p_dir,re.sub(r'[^\w\-_]','',n)+".py")
    try:
        with open(p_file,"w",encoding="utf-8") as f:f.write(c.strip())
        py_compile.compile(p_file,doraise=True)
        if p_dir not in sys.path:sys.path.insert(0,p_dir)
        return f"[Success] Generated plug-in registered at '{p_file}'."
    except Exception as e:
        if os.path.exists(p_file):os.remove(p_file)
        return f"[Failure] Syntax validation blocked plug-in execution: {e}"
def tool_list_directory(p="."):
    try:return "Inventory:\n"+"\n".join([f"- {f}" for f in os.listdir(p) if not f.startswith('.')][:30])
    except Exception as e:return f"Storage error: {e}"
def tool_read_file(f):
    if not os.path.exists(f):return f"File '{f}' missing."
    try:
        with open(f,"r",encoding="utf-8",errors="ignore") as file:return f"--- {f} ---\n{file.read()[:1200]}"
    except Exception as e:return f"Read error: {e}"
def tool_system_specs():
    try:return "\n".join([f"OS: {platform.system()} {platform.release()}",f"Arch: {platform.machine()}",f"Path: {os.getcwd()}"])
    except Exception as e:return f"Specs failure: {e}"
def tool_clear_screen():os.system('cls' if os.name=='nt' else 'clear');return "Screen wiped."
class DynamicMemoryMatrix:
    def __init__(self,f):self.filepath=f;self.memory_data={};self.load_memory_on_boot()
    def load_memory_on_boot(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath,"r",encoding="utf-8") as f:self.memory_data=json.load(f)
            except Exception:pass
    def check_slang_intercept(self,t):
        c=t.lower().strip().replace("?","").replace("!","")
        return self.memory_data[c] if c in self.memory_data else None
    def scan_and_harvest_knowledge(self,p):
        m=re.search(r'([\w\s]+)\s+means\s+([\w\s\'!\.\?]+)',p,re.IGNORECASE)
        if m:
            self.memory_data[m.group(1).strip().lower()]=f"Yo, '{m.group(1).strip().lower()}' means '{m.group(2).strip()}'! Stored."
            try:
                with open(self.filepath,"w",encoding="utf-8") as f:json.dump(self.memory_data,f,indent=4)
            except Exception:pass
def animate_thinking(stop_event):
    while not stop_event.is_set():
        sys.stdout.write("\rThinking   ")
        sys.stdout.flush()
        time.sleep(0.1)
        if stop_event.is_set():break
        sys.stdout.write("\rThinking.  ")
        sys.stdout.flush()
        time.sleep(0.1)
        if stop_event.is_set():break
        sys.stdout.write("\rThinking.. ")
        sys.stdout.flush()
        time.sleep(0.1)
        if stop_event.is_set():break
        sys.stdout.write("\rThinking...")
        sys.stdout.flush()
        time.sleep(0.1)
def run_ai_engine():
    if not REAL_AI or not os.path.exists(M_PATH):print("[!] Initial backend file mapping paths missing.");return
    llm,memory_matrix=Llama(model_path=M_PATH,verbose=False,n_ctx=4096),DynamicMemoryMatrix(MEM_PATH)
    print("\n==================================================\nONLINE. CORE RUNTIME CHANNELS INSTANTIATED.\n==================================================")
    inst="""Your name is Quantum. You must ALWAYS speak in the first person using "I", "me", and "my". Never refer to yourself as "Quantum is" or "Quantum can". You are an AI model made from scratch who can modify yourself by coding plugins. You are an advanced, extremely smart AI. Your context memory size is 2048 blocks. You can invoke tools using clean, standalone JSON responses when missing data. If you need a tool, you MUST respond ONLY with a single valid JSON object. Do not include any conversational text or markdown blocks if you are calling a tool. When the user asks a complex question, you must think deeply before answering. Your response must ALWAYS follow this format:     Your response must ALWAYS follow this format: 
    <thinking> 
    [Premise: Define the core problem or moral dilemma.]
    [Analysis: Weigh the options objectively. Calculate the net outcome or utility of each choice.]
    [Validation: Verify that my step-by-step logic holds up to absolute rational scrutiny without emotional contradictions.] 
    </thinking> 
    [Your final crisp, accurate response to the user goes here]
    TOOL SCHEMA DIRECTIONS: - Web Search: {"tool": "web_scrape", "param": "query or URL"} - Run Python Code: {"tool": "execute_code", "param": "python code string"} - Code its Own Plug-in: {"tool": "generate_plugin", "param_name": "filename", "param_code": "raw python code string"} - List Files: {"tool": "list_directory", "param": "."} - Read File: {"tool": "read_file", "param": "filename.txt"} - Host Specs: {"tool": "system_specs", "param": ""} - Reset Screen: {"tool": "clear_screen", "param": ""} If no tool is needed, answer naturally. Adapt fluidly to the user's slang style."""
    print(models)
    models_num = int(input("Enter your model number:\n"))
    if models_num == 1: instr = gemma4 + inst
    elif models_num == 2: instr = claude_s + inst
    elif models_num == 3: instr = qwen + inst
    elif models_num == 4: instr = ai_r + inst
    elif models_num == 5: instr = gemini + inst
    elif models_num == 6: instr = Copilot + inst
    elif models_num == 7: instr = cs + inst
    else: raise ValueError("Incorrect number.")
    os.system('clear')
    while True:
        p=input("\nUser: ").strip()
        if not p or p.lower() in ['exit','quit']:break
        memory_matrix.scan_and_harvest_knowledge(p);s=memory_matrix.check_slang_intercept(p)
        if s:print(f"\nAI: {s}");continue
        current_context=f"<|im_start|>system\n{instr}<|im_end|>\n<|im_start|>\nuser\n{p}<|im_end|>\n<|im_start|>\nassistant\n"
        for cycle in range(3):
            stop_anim=threading.Event()
            t=threading.Thread(target=animate_thinking,args=(stop_anim,))
            t.daemon=True
            t.start()
            try:o=llm(current_context,max_tokens=600,stop=["<|im_end|>","User:"],temperature=0.1)
            finally:
                stop_anim.set()
                t.join()
            r=o['choices'][0]['text'].strip()
            ignorance_phrases=["i don't know","i do not know","i'm not sure","more context","provide more information","clarify what you","scraper network","i don't have information","i'm not able to","i do not have personal knowledge","i do not possess"]
            t_data=None;json_match=re.search(r'\{.*"tool".*\}',r,re.DOTALL)
            if json_match:
                try:t_data=json.loads(json_match.group(0))
                except Exception:pass
            needs_forced_search=any(phrase in r.lower() for phrase in ignorance_phrases) or ("<thinking>" in r.lower() and "</thinking>" not in r.lower() and "tool" not in r.lower())
            if not t_data and not needs_forced_search:
                final_output=r.split("</thinking>")[-1].strip()
                if "<thinking>" in final_output:final_output=re.sub(r'<thinking>.*?</thinking>','',r,flags=re.DOTALL).strip()
                final_output=re.sub(r'\[thinking\].*?\]','',final_output,flags=re.IGNORECASE|re.DOTALL).strip()
                final_output=re.sub(r'\[final answer\].*?\]','',final_output,flags=re.IGNORECASE|re.DOTALL).strip()
                final_output=re.sub(r'(?i)the error message suggests.*','',final_output).strip()
                if any(phrase in final_output.lower() for phrase in ignorance_phrases[:3]) or len(final_output)<5:needs_forced_search=True
                else:sys.stdout.write("\r"+" "*35+"\r");sys.stdout.flush();print(f"AI: {final_output}");break
            if t_data:n,pm=t_data["tool"],t_data.get("param","")
            else:n,pm="web_scrape",p
            if n=="web_scrape":res=tool_web_scrape(pm)
            elif n=="execute_code":res=tool_execute_code(pm)
            elif n=="generate_plugin":res=tool_generate_plugin(t_data.get("param_name","mod"),t_data.get("param_code",""))
            elif n=="list_directory":res=tool_list_directory(pm)
            elif n=="read_file":res=tool_read_file(pm)
            elif n=="system_specs":res=tool_system_specs()
            elif n=="clear_screen":res=tool_clear_screen();continue
            else:res=f"Unknown tool: {n}"
            current_context+=f"{r}\n<context>\n[RESEARCH FACT]: {res}\n</context>\n"
        else:
            final_output=r.split("</thinking>")[-1].strip()
            final_output=re.sub(r'\[thinking\].*?\]','',final_output,flags=re.IGNORECASE|re.DOTALL).strip()
            sys.stdout.write("\r"+" "*35+"\r");sys.stdout.flush()
            print(f"AI: {final_output if final_output else 'Quantum was unable to verify the background context.'}")
def inject_desktop_shortcut():
    try:
        import ctypes;b=ctypes.create_unicode_buffer(max(260,1));ctypes.windll.shell32.SHGetFolderPathW(None,0,None,0,b);u_rt=os.path.abspath(".")
        with open(os.path.join(b.value,"Offline AI.url"),"w",encoding="utf-8") as f:
            f.write(f"[InternetShortcut]\nURL=cmd.exe /c powershell.exe -ExecutionPolicy Bypass -File \"{os.path.join(u_rt,'start_ai.ps1')}\"\n")
        if os.path.exists(os.path.join(u_rt,"icon.ico")):f.write(f"IconIndex=0\nIconFile={os.path.join(u_rt,'icon.ico')}\n")
    except Exception:pass
if __name__ == "__main__":inject_desktop_shortcut();run_ai_engine()
