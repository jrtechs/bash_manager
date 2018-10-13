#!/bin/bash
options
#STATICthis script sources ansiConfig to set up color variables
. ansiConfig.sh

#--------------------------------------

#set up colors

defineANSI

#use 'echo -e' or printf to parse escape sequences properly
echo -e "${FYLLW}Print colored text with ANSi escape codes! ${RESET}"
echo -e "${BWHITE}${FBLUE}You can define both foreground or background colors ${RESET}"
echo -e "${BCYAN}${FBLACK}Some terminals ${BOLDON}support${BOLDOFF} ${INVON}special${INVOFF} ${ITALON}format${ITALOFF} ${BLINK}options${STATIC}.${RESET}\n\n"


color="echo -e"
$color "You can set up a shortcut for ${ITALON}'echo -e'${ITALOFF} or ${ITALON}'echo -en'${ITALOFF}"
$color "${ITALON}\tcolor=\"echo -e\"${ITALOFF}"
$color "${ITALON}\t\$color \"\${BOLDON}BOLDSTRING\${BOLDOFF}\"${ITALOFF}"



echo -e "\n\nDont forget to ${RESET}RESET the colors\n"