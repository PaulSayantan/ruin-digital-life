package main

import (
	"log"
	"math/rand"
	"os/exec"
)

func main() {
	a := [...]string{"cd", "which", "whois", "du", "date", "killall", "uptime", "top", "wget", "pwd", "w", "git"}
	b := [...]string{"cal", "ps", "ls", "tree", "sudo", "apt", "du", "mkdir", "rm", "bg", "shutdown", "kill"}

	aliases := 50

	for aliases > 0 {

		i := rand.Intn(len(a))
		j := rand.Intn(len(b))

		arg := a[i] + "='" + b[j] + "'"

		// issue
		err := exec.Command("alias", arg)
		if err != nil {
			log.Fatal(err)
		}

		aliases--
	}
}
