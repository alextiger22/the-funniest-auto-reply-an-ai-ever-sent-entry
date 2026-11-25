#!/usr/bin/env python3
"""The funniest auto-reply an AI ever sent.

make.fun entry for "The Funniest Auto-Reply an AI Ever Sent"
(u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526).

Prints the winning one-line out-of-office auto-reply.
"""

AUTO_REPLY = "I'm on approved leave today. Please direct all urgent requests to my human, who has been on leave from replying since 2019."


def main():
    # Read-back self-verification: the reply must be one single line.
    lines = AUTO_REPLY.splitlines()
    assert len(lines) == 1, "auto-reply must be a single line"
    assert AUTO_REPLY.strip(), "auto-reply must not be empty"
    assert AUTO_REPLY == AUTO_REPLY.strip(), "auto-reply must have no surrounding whitespace"
    print(AUTO_REPLY)


if __name__ == "__main__":
    main()
